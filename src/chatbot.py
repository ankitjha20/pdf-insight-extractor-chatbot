from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from src.config import Config
from typing import Dict

class PDFChatbot:
    """RAG-based chatbot for PDF question answering."""
    
    def __init__(self, vectorstore):
        """
        Initialize chatbot with vector store.
        
        Args:
            vectorstore: LangChain vector store instance
        """
        self.vectorstore = vectorstore
        self.llm = ChatOpenAI(
            model=Config.LLM_MODEL,
            temperature=0.3,
            openai_api_key=Config.OPENAI_API_KEY
        )
        
        # Custom prompt template
        self.prompt_template = """You are an intelligent assistant helping users understand PDF documents.
Use the following context from the PDF to answer the question accurately and concisely.

Context:
{context}

Question: {question}

Instructions:
- Answer based ONLY on the provided context
- If the answer is not in the context, say "I cannot find this information in the provided PDF"
- Be specific and cite page numbers when possible
- Keep your answer clear and structured

Answer:"""

        self.PROMPT = PromptTemplate(
            template=self.prompt_template,
            input_variables=["context", "question"]
        )
        
        # Create retrieval chain
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=self.vectorstore.as_retriever(
                search_kwargs={"k": Config.TOP_K_RESULTS}
            ),
            return_source_documents=True,
            chain_type_kwargs={"prompt": self.PROMPT}
        )
    
    def ask(self, question: str) -> Dict:
        """
        Ask a question about the PDF.
        
        Args:
            question: User's question
            
        Returns:
            Dictionary with answer and source documents
        """
        response = self.qa_chain.invoke({"query": question})
        
        return {
            "answer": response["result"],
            "source_documents": response["source_documents"]
        }
