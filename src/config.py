import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Configuration management for the PDF chatbot."""
    
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    EMBEDDING_MODEL = "text-embedding-3-small"
    LLM_MODEL = "gpt-4o-mini"
    CHUNK_SIZE = 1000
    CHUNK_OVERLAP = 200
    TOP_K_RESULTS = 4
    CHROMA_PERSIST_DIR = "./db/chroma_db"
    UPLOAD_DIR = "./data/uploads"
    
    @staticmethod
    def validate():
        """Validate required environment variables."""
        if not Config.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY not found in environment variables")
