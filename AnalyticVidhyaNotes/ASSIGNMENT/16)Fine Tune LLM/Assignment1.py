import torch
from datasets import load_dataset
from transformers import (
    AutoModelForSequenceClassification,
    AutoTokenizer,
    TrainingArguments,
    Trainer,
    DataCollatorWithPadding
)
from peft import (
    LoraConfig,
    get_peft_model,
    prepare_model_for_kbit_training,
    TaskType
)
import evaluate
import numpy as np
from sklearn.metrics import classification_report

# 1. Load and prepare dataset
def prepare_dataset():

    # Load dataset from Hugging Face
    dataset = load_dataset("FinGPT/fingpt-sentiment-train")
    
    # Load tokenizer
    tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-v0.1")
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    # Preprocess function
    def preprocess_function(examples):
        return tokenizer(
            examples["text"],
            truncation=True,
            padding=True,
            max_length=512
        )

    # Tokenize datasets
    tokenized_dataset = dataset.map(
        preprocess_function,
        batched=True,
        remove_columns=dataset["train"].column_names
    )

    return tokenized_dataset, tokenizer

# 2. Configure and prepare model with LoRA
def prepare_model():
    # Load base model
    model = AutoModelForSequenceClassification.from_pretrained(
        "mistralai/Mistral-7B-v0.1",
        num_labels=3,  # Negative, Neutral, Positive
        torch_dtype=torch.float16,
        device_map="auto"
    )

    # Configure LoRA
    lora_config = LoraConfig(
        r=16,  # Rank
        lora_alpha=32,
        target_modules=["q_proj", "v_proj"],
        lora_dropout=0.05,
        bias="none",
        task_type=TaskType.SEQ_CLS
    )

    # Prepare model for training
    model = prepare_model_for_kbit_training(model)
    model = get_peft_model(model, lora_config)
    
    return model

# 3. Define metrics computation
def compute_metrics(eval_pred):
    predictions, labels = eval_pred
    predictions = np.argmax(predictions, axis=1)
    
    accuracy = evaluate.load("accuracy")
    f1 = evaluate.load("f1")
    
    return {
        "accuracy": accuracy.compute(predictions=predictions, references=labels)["accuracy"],
        "f1": f1.compute(predictions=predictions, references=labels, average="weighted")["f1"]
    }

# 4. Training function
def train_model(model, tokenized_dataset, tokenizer):
    training_args = TrainingArguments(
        output_dir="./mistral-sentiment-finetuned",
        learning_rate=2e-4,
        per_device_train_batch_size=4,
        per_device_eval_batch_size=4,
        num_train_epochs=3,
        weight_decay=0.01,
        evaluation_strategy="epoch",
        save_strategy="epoch",
        load_best_model_at_end=True,
        push_to_hub=False,
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset["train"],
        eval_dataset=tokenized_dataset["validation"],
        tokenizer=tokenizer,
        data_collator=DataCollatorWithPadding(tokenizer=tokenizer),
        compute_metrics=compute_metrics,
    )

    # Train the model
    trainer.train()
    
    return trainer

# 5. Evaluation function
def evaluate_model(trainer, tokenized_dataset):
    # Evaluate on test set
    test_results = trainer.evaluate(tokenized_dataset["test"])
    
    # Get predictions for detailed classification report
    predictions = trainer.predict(tokenized_dataset["test"])
    pred_labels = np.argmax(predictions.predictions, axis=1)
    true_labels = predictions.label_ids
    
    # Generate classification report
    target_names = ["Negative", "Neutral", "Positive"]
    report = classification_report(true_labels, pred_labels, target_names=target_names)
    
    return test_results, report

# Main execution
def main():
    # 1. Prepare dataset
    print("Preparing dataset...")
    tokenized_dataset, tokenizer = prepare_dataset()
    
    # 2. Prepare model
    print("Preparing model...")
    model = prepare_model()
    
    # 3. Train model
    print("Training model...")
    trainer = train_model(model, tokenized_dataset, tokenizer)
    
    # 4. Evaluate model
    print("Evaluating model...")
    test_results, classification_report = evaluate_model(trainer, tokenized_dataset)
    
    # Print results
    print("\nTest Results:", test_results)
    print("\nClassification Report:\n", classification_report)
    
    # Save model
    trainer.save_model("./final-model")
    
if __name__ == "__main__":
    main()