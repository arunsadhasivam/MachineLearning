import torch
from datasets import load_dataset
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    TrainingArguments,
    Trainer,
    DataCollatorForLanguageModeling
)
from peft import (
    LoraConfig,
    get_peft_model,
    prepare_model_for_kbit_training
)
import evaluate
import numpy as np
from tqdm import tqdm

class FinanceDataset(torch.utils.data.Dataset):
    def __init__(self, data, tokenizer, max_length=512):
        self.data = data
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        item = self.data[idx]
        # Format: Create instruction format similar to Alpaca
        prompt = f"""Below is a financial question that needs to be answered:

Question: {item['question']}

Please provide a detailed and accurate answer based on financial knowledge.

Answer: {item['answer']}

"""
        # Tokenize
        encodings = self.tokenizer(
            prompt,
            truncation=True,
            max_length=self.max_length,
            padding="max_length",
            return_tensors="pt"
        )
        
        # Create labels (same as input_ids for causal LM)
        encodings["labels"] = encodings["input_ids"].clone()
        
        # Convert to pytorch tensors
        return {
            "input_ids": encodings["input_ids"][0],
            "attention_mask": encodings["attention_mask"][0],
            "labels": encodings["labels"][0]
        }

def prepare_dataset():
    """Load and prepare the FiQA dataset"""
    # Load dataset
    dataset = load_dataset("FinGPT/fingpt-fiqa_qa")
    
    # Load tokenizer
    tokenizer = AutoTokenizer.from_pretrained(
        "google/gemma-2b",
        trust_remote_code=True
    )
    tokenizer.pad_token = tokenizer.eos_token
    
    # Create custom datasets
    train_dataset = FinanceDataset(dataset["train"], tokenizer)
    eval_dataset = FinanceDataset(dataset["validation"], tokenizer)
    
    return train_dataset, eval_dataset, tokenizer

def prepare_model():
    """Configure and prepare model with QLoRA"""
    # Configure 4-bit quantization
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_use_double_quant=True,
        bnb_4bit_compute_dtype=torch.bfloat16
    )
    
    # Load base model with quantization
    model = AutoModelForCausalLM.from_pretrained(
        "google/gemma-2b",
        quantization_config=bnb_config,
        device_map="auto",
        trust_remote_code=True
    )
    
    # Configure LoRA
    lora_config = LoraConfig(
        r=64,  # Rank
        lora_alpha=16,
        target_modules=["q_proj", "v_proj", "k_proj", "o_proj"],
        lora_dropout=0.05,
        bias="none",
        task_type="CAUSAL_LM"
    )
    
    # Prepare model for training
    model = prepare_model_for_kbit_training(model)
    model = get_peft_model(model, lora_config)
    
    return model

def train_model(model, train_dataset, eval_dataset, tokenizer):
    """Train the model using QLoRA"""
    training_args = TrainingArguments(
        output_dir="./gemma-fiqa-finetuned",
        num_train_epochs=3,
        per_device_train_batch_size=4,
        per_device_eval_batch_size=4,
        gradient_accumulation_steps=4,
        learning_rate=2e-4,
        fp16=True,
        logging_steps=100,
        evaluation_strategy="steps",
        eval_steps=500,
        save_strategy="steps",
        save_steps=500,
        warmup_steps=100,
        load_best_model_at_end=True,
        optim="paged_adamw_32bit",
        lr_scheduler_type="cosine",
        weight_decay=0.05,
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,
        data_collator=DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)
    )
    
    # Train the model
    trainer.train()
    
    return trainer

def evaluate_model(trainer, eval_dataset, tokenizer):
    """Evaluate model performance"""
    # Generate predictions for a sample of evaluation data
    model = trainer.model
    model.eval()
    
    results = []
    sample_size = min(50, len(eval_dataset))  # Evaluate on 50 samples
    
    for i in tqdm(range(sample_size)):
        item = eval_dataset[i]
        input_text = tokenizer.decode(item["input_ids"], skip_special_tokens=True)
        question = input_text.split("Question: ")[1].split("Please provide")[0].strip()
        
        # Generate answer
        inputs = tokenizer(
            f"Question: {question}\n\nAnswer:",
            return_tensors="pt",
            truncation=True,
            max_length=512
        ).to("cuda")
        
        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_new_tokens=200,
                temperature=0.7,
                num_return_sequences=1,
                pad_token_id=tokenizer.eos_token_id
            )
        
        generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        answer = generated_text.split("Answer:")[1].strip()
        
        # Store results
        results.append({
            "question": question,
            "generated_answer": answer,
            "reference_answer": input_text.split("Answer: ")[1].strip()
        })
    
    return results

def main():
    # 1. Prepare dataset
    print("Preparing dataset...")
    train_dataset, eval_dataset, tokenizer = prepare_dataset()
    
    # 2. Prepare model
    print("Preparing model...")
    model = prepare_model()
    
    # 3. Train model
    print("Training model...")
    trainer = train_model(model, train_dataset, eval_dataset, tokenizer)
    
    # 4. Evaluate model
    print("Evaluating model...")
    evaluation_results = evaluate_model(trainer, eval_dataset, tokenizer)
    
    # 5. Save results
    import json
    with open("evaluation_results.json", "w") as f:
        json.dump(evaluation_results, f, indent=2)
    
    # 6. Save model
    trainer.save_model("./final-model")
    
if __name__ == "__main__":
    main()