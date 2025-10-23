import streamlit as st
from typing import Optional

def initialize_session_state():
    """Initialize Streamlit session state variables."""
    if "vectorstore" not in st.session_state:
        st.session_state.vectorstore = None
    if "chatbot" not in st.session_state:
        st.session_state.chatbot = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "pdf_processed" not in st.session_state:
        st.session_state.pdf_processed = False

def display_chat_message(role: str, content: str):
    """Display a chat message with appropriate styling."""
    with st.chat_message(role):
        st.markdown(content)

def format_sources(source_documents) -> str:
    """Format source documents for display."""
    if not source_documents:
        return ""
    
    sources_text = "\n\n**📄 Sources:**\n"
    for i, doc in enumerate(source_documents, 1):
        preview = doc.page_content[:150].replace("\n", " ")
        sources_text += f"{i}. {preview}...\n"
    
    return sources_text
