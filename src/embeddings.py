from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from src.config import Config
from typing import List

class EmbeddingManager:
    """Manages text chunking and vector store operations."""
    
    def __init__(self):
        self.embeddings = OpenAIEmbeddings(
            model=Config.EMBEDDING_MODEL,
            openai_api_key=Config.OPENAI_API_KEY
        )
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=Config.CHUNK_SIZE,
            chunk_overlap=Config.CHUNK_OVERLAP,
            length_function=len,
            separators=["\n\n", "\n", " ", ""]
        )
    
    def create_vector_store(self, text: str, collection_name: str = "pdf_collection") -> Chroma:
        """
        Create vector store from text.
        
        Args:
            text: Raw text to process
            collection_name: Name for the Chroma collection
            
        Returns:
            Chroma vector store instance
        """
        # Split text into chunks
        chunks = self.text_splitter.split_text(text)
        
        # Create vector store
        vectorstore = Chroma.from_texts(
            texts=chunks,
            embedding=self.embeddings,
            collection_name=collection_name,
            persist_directory=Config.CHROMA_PERSIST_DIR
        )
        
        return vectorstore
    
    def load_vector_store(self, collection_name: str = "pdf_collection") -> Chroma:
        """
        Load existing vector store from disk.
        
        Args:
            collection_name: Name of the collection to load
            
        Returns:
            Loaded Chroma vector store
        """
        vectorstore = Chroma(
            collection_name=collection_name,
            embedding_function=self.embeddings,
            persist_directory=Config.CHROMA_PERSIST_DIR
        )
        
        return vectorstore
