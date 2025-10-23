from PyPDF2 import PdfReader
from typing import List
import os

class PDFProcessor:
    """Handles PDF text extraction and preprocessing."""
    
    @staticmethod
    def extract_text(pdf_path: str) -> str:
        """
        Extract text from PDF file.
        
        Args:
            pdf_path: Path to the PDF file
            
        Returns:
            Extracted text as a single string
        """
        try:
            reader = PdfReader(pdf_path)
            text = ""
            
            for page_num, page in enumerate(reader.pages):
                page_text = page.extract_text()
                if page_text:
                    text += f"\n--- Page {page_num + 1} ---\n{page_text}"
            
            return text.strip()
        
        except Exception as e:
            raise Exception(f"Error extracting text from PDF: {str(e)}")
    
    @staticmethod
    def save_uploaded_file(uploaded_file, save_dir: str) -> str:
        """
        Save uploaded file to disk.
        
        Args:
            uploaded_file: Streamlit uploaded file object
            save_dir: Directory to save the file
            
        Returns:
            Path to saved file
        """
        os.makedirs(save_dir, exist_ok=True)
        file_path = os.path.join(save_dir, uploaded_file.name)
        
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        return file_path
