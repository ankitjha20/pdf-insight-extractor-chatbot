__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
import streamlit as st
from src.config import Config
from src.pdf_processor import PDFProcessor
from src.embeddings import EmbeddingManager
from src.chatbot import PDFChatbot
from utils.helpers import initialize_session_state, display_chat_message, format_sources

# Page configuration
st.set_page_config(
    page_title="PDF Insight Extractor",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Validate configuration
try:
    Config.validate()
except ValueError as e:
    st.error(f"⚠️ Configuration Error: {str(e)}")
    st.stop()

# Initialize session state
initialize_session_state()

# Sidebar
with st.sidebar:
    st.title("📄 PDF Insight Extractor")
    st.markdown("---")
    
    # File uploader
    uploaded_file = st.file_uploader(
        "Upload your PDF",
        type=["pdf"],
        help="Upload a PDF document to chat with"
    )
    
    if uploaded_file:
        if st.button("🔄 Process PDF", type="primary"):
            with st.spinner("Processing PDF..."):
                try:
                    # Save and extract text
                    pdf_path = PDFProcessor.save_uploaded_file(
                        uploaded_file,
                        Config.UPLOAD_DIR
                    )
                    pdf_text = PDFProcessor.extract_text(pdf_path)
                    
                    # Create embeddings and vector store
                    embedding_manager = EmbeddingManager()
                    vectorstore = embedding_manager.create_vector_store(pdf_text)
                    
                    # Initialize chatbot
                    st.session_state.vectorstore = vectorstore
                    st.session_state.chatbot = PDFChatbot(vectorstore)
                    st.session_state.pdf_processed = True
                    st.session_state.chat_history = []
                    
                    st.success("✅ PDF processed successfully!")
                
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
    
    st.markdown("---")
    
    # Info section
    if st.session_state.pdf_processed:
        st.success("🟢 PDF Loaded")
        st.info(f"**Model:** {Config.LLM_MODEL}")
    else:
        st.warning("🟡 No PDF loaded")
    
    # Clear chat button
    if st.button("🗑️ Clear Chat History"):
        st.session_state.chat_history = []
        st.rerun()

# Main content
st.title("💬 Chat with Your PDF")

if not st.session_state.pdf_processed:
    st.info("👈 Please upload and process a PDF from the sidebar to begin chatting.")
else:
    # Display chat history
    for message in st.session_state.chat_history:
        display_chat_message(message["role"], message["content"])
    
    # Chat input
    if prompt := st.chat_input("Ask a question about your PDF..."):
        # Display user message
        display_chat_message("user", prompt)
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        
        # Get chatbot response
        with st.spinner("Thinking..."):
            try:
                response = st.session_state.chatbot.ask(prompt)
                answer = response["answer"]
                sources = format_sources(response["source_documents"])
                
                full_response = answer + sources
                
                # Display assistant message
                display_chat_message("assistant", full_response)
                st.session_state.chat_history.append({
                    "role": "assistant",
                    "content": full_response
                })
            
            except Exception as e:
                error_msg = f"❌ Error: {str(e)}"
                display_chat_message("assistant", error_msg)

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: gray;'>
        Built with LangChain, OpenAI, ChromaDB & Streamlit
    </div>
    """,
    unsafe_allow_html=True
)
