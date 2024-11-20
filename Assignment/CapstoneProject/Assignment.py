# Import required libraries
import streamlit as st
import os
import requests
import tempfile
from typing import List, Dict, Any, Optional, Union
from dataclasses import dataclass
from enum import Enum
import torch
from sentence_transformers import SentenceTransformer, util
import faiss
import numpy as np
from transformers import (
    AutoTokenizer, 
    AutoModelForSequenceClassification,
    AutoModelForCausalLM
)
from pypdf import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import openai
from pathlib import Path
from dotenv import load_dotenv, find_dotenv
import os

class EmbeddingType(Enum):
    """Available embedding models"""
    MINILM = "all-MiniLM-L6-v2"
    MPNet = "all-mpnet-base-v2"
    OPENAI = "text-embedding-3-small"

class SearchType(Enum):
    """Available search strategies"""
    COSINE = "cosine"
    HYBRID = "hybrid"
    RERANKER = "reranker"

@dataclass
class Document:
    """Document storage class"""
    text: str
    source: str
    page_number: int
    embedding: Optional[np.ndarray] = None

class PDFLoader:
    """Handles PDF loading from various sources"""
    
    @staticmethod
    def load_from_file(file) -> List[Document]:
        """Load PDF from uploaded file"""
        pdf_reader = PdfReader(file)
        documents = []
        
        for page_num, page in enumerate(pdf_reader.pages):
            text = page.extract_text()
            if text.strip():  # Only add non-empty pages
                documents.append(Document(
                    text=text,
                    source=file.name,
                    page_number=page_num + 1
                ))
                
        return documents
    
    @staticmethod
    def load_from_url(url: str) -> List[Document]:
        """Load PDF from URL"""
        response = requests.get(url)
        with tempfile.NamedTemporaryFile(suffix=".pdf") as temp_file:
            temp_file.write(response.content)
            temp_file.seek(0)
            return PDFLoader.load_from_file(temp_file)

class TextProcessor:
    """Handles text preprocessing and chunking"""
    
    def __init__(self, chunk_size: int = 500, chunk_overlap: int = 50):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )
    
    def process_documents(self, documents: List[Document]) -> List[Document]:
        """Split documents into chunks"""
        processed_documents = []
        
        for doc in documents:
            chunks = self.text_splitter.split_text(doc.text)
            for chunk in chunks:
                processed_documents.append(Document(
                    text=chunk,
                    source=doc.source,
                    page_number=doc.page_number
                ))
                
        return processed_documents

class EmbeddingManager:
    """Handles document embedding generation"""
    
    def __init__(self, embedding_type: EmbeddingType):
        self.embedding_type = embedding_type
        self.model = self._initialize_model()
        
    def _initialize_model(self):
        """Initialize the selected embedding model"""
        if self.embedding_type == EmbeddingType.OPENAI:
            return None  # OpenAI embeddings are handled via API
        return SentenceTransformer(self.embedding_type.value)
    
    def generate_embeddings(self, documents: List[Document]) -> List[Document]:
        """Generate embeddings for documents"""
        if self.embedding_type == EmbeddingType.OPENAI:
            # Use OpenAI API for embeddings
            for doc in documents:
                response = openai.Embedding.create(
                    model="text-embedding-3-small",
                    input=doc.text
                )
                doc.embedding = np.array(response['data'][0]['embedding'])
        else:
            # Use local models
            texts = [doc.text for doc in documents]
            embeddings = self.model.encode(texts)
            for doc, embedding in zip(documents, embeddings):
                doc.embedding = embedding
                
        return documents

class VectorStore:
    """Manages vector storage and retrieval"""
    
    def __init__(self, dimension: int):
        self.index = faiss.IndexFlatL2(dimension)
        self.documents: List[Document] = []
        
    def add_documents(self, documents: List[Document]):
        """Add documents to the vector store"""
        embeddings = np.vstack([doc.embedding for doc in documents])
        self.index.add(embeddings)
        self.documents.extend(documents)
    
    def search(
        self,
        query_embedding: np.ndarray,
        k: int = 3,
        search_type: SearchType = SearchType.COSINE
    ) -> List[tuple[Document, float]]:
        """Search for similar documents"""
        # Perform initial vector search
        distances, indices = self.index.search(
            query_embedding.reshape(1, -1),
            k
        )
        
        results = [
            (self.documents[idx], float(dist))
            for idx, dist in zip(indices[0], distances[0])
        ]
        
        return results

class Reranker:
    """Handles document reranking"""
    
    def __init__(self):
        self.model = AutoModelForSequenceClassification.from_pretrained(
            'cross-encoder/ms-marco-MiniLM-L-6-v2'
        )
        self.tokenizer = AutoTokenizer.from_pretrained(
            'cross-encoder/ms-marco-MiniLM-L-6-v2'
        )
        
    def rerank(
        self,
        query: str,
        documents: List[tuple[Document, float]]
    ) -> List[tuple[Document, float]]:
        """Rerank documents using cross-encoder"""
        pairs = [
            [query, doc.text] 
            for doc, _ in documents
        ]
        
        features = self.tokenizer(
            pairs,
            padding=True,
            truncation=True,
            return_tensors="pt",
            max_length=512
        )
        
        with torch.no_grad():
            scores = self.model(**features).logits
            
        reranked_results = [
            (doc, float(score))
            for (doc, _), score in zip(documents, scores)
        ]
        
        return sorted(reranked_results, key=lambda x: x[1], reverse=True)

class RAGPipeline:
    """Main RAG pipeline class"""
    

    def __init__(
        self,
        embedding_type: EmbeddingType,
        llm_model: str = "microsoft/phi-2"
    ):
        self.pdf_loader = PDFLoader()
        self.text_processor = TextProcessor()
        self.embedding_manager = EmbeddingManager(embedding_type)
        self.vector_store = None  # Initialized after first documents
        self.reranker = Reranker()
        
        # Initialize LLM
        self.tokenizer = AutoTokenizer.from_pretrained(llm_model)
        self.llm = AutoModelForCausalLM.from_pretrained(llm_model)
        
    def process_document(
        self,
        file_or_url: Union[str, Any],
        is_url: bool = False
    ):
        """Process new document"""
        # Load document
        if is_url:
            documents = self.pdf_loader.load_from_url(file_or_url)
        else:
            documents = self.pdf_loader.load_from_file(file_or_url)
        
        # Process and chunk documents
        documents = self.text_processor.process_documents(documents)
        
        # Generate embeddings
        documents = self.embedding_manager.generate_embeddings(documents)
        
        # Initialize or update vector store
        if self.vector_store is None:
            self.vector_store = VectorStore(documents[0].embedding.shape[0])
        self.vector_store.add_documents(documents)
        
    def search(
        self,
        query: str,
        search_type: SearchType,
        k: int = 3
    ) -> List[tuple[Document, float]]:
        """Search for relevant documents"""
        # Generate query embedding
        query_embedding = self.embedding_manager.model.encode([query])[0]
        
        # Initial vector search
        results = self.vector_store.search(
            query_embedding,
            k=k if search_type != SearchType.HYBRID else k * 2,
            search_type=search_type
        )
        
        # Apply reranking if requested
        if search_type in [SearchType.RERANKER, SearchType.HYBRID]:
            results = self.reranker.rerank(query, results)
            results = results[:k]
        
        return results
    
    def generate_response(
        self,
        query: str,
        contexts: List[tuple[Document, float]]
    ) -> str:
        """Generate response using LLM"""
        # Prepare context
        context_text = "\n\n".join([
            f"Source: {doc.source} (Page {doc.page_number})\n{doc.text}"
            for doc, _ in contexts
        ])
        
        # Create prompt
        prompt = f"""Context: {context_text}

Question: {query}

Please provide a detailed answer based on the context above. Include citations to the source documents where appropriate.

Answer:"""
        
        # Generate response
        inputs = self.tokenizer(prompt, return_tensors="pt")
        outputs = self.llm.generate(
            **inputs,
            max_length=512,
            num_return_sequences=1,
            temperature=0.7
        )
        
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response

class RAGInterface:
    """Streamlit interface for RAG system"""
    
    def __init__(self):
        self.rag_pipeline = None
        load_dotenv('../security/.env')
        # self.OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
        #self.OPENAI_API_KEY_GOOGLE = os.environ["OPENAI_API_KEY_GOOGLE"]
        
    def run(self):
        """Run the Streamlit interface"""
        st.title("📚 RAG System")
        
        # Sidebar configuration
        with st.sidebar:
            st.header("Configuration")
            
            # Embedding model selection
            embedding_model = st.selectbox(
                "Embedding Model",
                options=[e.value for e in EmbeddingType],
                format_func=lambda x: x.split('/')[-1]
            )
            
            # OpenAI API key input if needed
            if embedding_model == EmbeddingType.OPENAI.value:
                openai.api_key =  os.environ["OPENAI_API_KEY"]
            
            # Initialize RAG pipeline
            if not self.rag_pipeline:
                self.rag_pipeline = RAGPipeline(
                    EmbeddingType(embedding_model)
                )
        
        
        # Main interface
        tab1, tab2 = st.tabs(["📄 Document Upload", "🔍 Search"])
        
        # Document Upload Tab
        with tab1:
            st.header("Upload Documents")
            
            # File upload
            uploaded_files = st.file_uploader(
                "Upload PDF files",
                type="pdf",
                accept_multiple_files=True
            )
            
            # URL input
            url = st.text_input("Or enter PDF URL")
            
            if st.button("Process Documents"):
                with st.spinner("Processing documents..."):
                    if uploaded_files:
                        for file in uploaded_files:
                            self.rag_pipeline.process_document(file)
                            st.success(f"Processed {file.name}")
                            
                    if url:
                        self.rag_pipeline.process_document(url, is_url=True)
                        st.success(f"Processed {url}")
        
        # Search Tab
        with tab2:
            st.header("Search and Query")
            
            # Search configuration
            search_type = st.selectbox(
                "Search Strategy",
                options=[s.value for s in SearchType]
            )
            
            # Query input
            query = st.text_input("Enter your query")
            
            if query and st.button("Search"):
                if not self.rag_pipeline or not self.rag_pipeline.vector_store:
                    st.error("Please upload documents first!")
                    return
                
                with st.spinner("Searching..."):
                    # Perform search
                    results = self.rag_pipeline.search(
                        query,
                        SearchType(search_type)
                    )
                    
                    # Generate response
                    response = self.rag_pipeline.generate_response(
                        query,
                        results
                    )
                    
                    # Display results
                    st.subheader("Response")
                    st.write(response)
                    
                    st.subheader("Source Documents")
                    for doc, score in results:
                        with st.expander(
                            f"Source: {doc.source} (Page {doc.page_number})"
                        ):
                            st.write(f"Relevance Score: {score:.3f}")
                            st.write(doc.text)

if __name__ == "__main__":
    interface = RAGInterface()
    interface.run()