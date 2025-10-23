📄 PDF Insight Extractor: An Intelligent RAG Chatbot
<p align="center"> <img src="https://i.imgur.com/your-gif-url.gif" alt="PDF Insight Extractor Demo"> </p> <p align="center"> <img src="https://img.shields.io/badge/Python-3.11%2B-blue?style=for-the-badge&logo=python" alt="Python Version"> <img src="https://img.shields.io/badge/LangChain-v0.3-orange?style=for-the-badge" alt="LangChain"> <img src="https://img.shields.io/badge/OpenAI-GPT--4-green?style=for-the-badge&logo=openai" alt="OpenAI"> <img src="https://img.shields.io/badge/Database-ChromaDB-purple?style=for-the-badge" alt="ChromaDB"> <img src="https://img.shields.io/badge/UI-Streamlit-red?style=for-the-badge&logo=streamlit" alt="Streamlit"> </p>
An advanced Retrieval-Augmented Generation (RAG) application that transforms any PDF document into an interactive chatbot. Upload a PDF and ask complex questions, get summaries, and find specific information in seconds. Built with LangChain, OpenAI, ChromaDB, and Streamlit.

✨ Key Features
Interactive Chat Interface: A user-friendly, real-time chat experience powered by Streamlit.

Dynamic PDF Processing: Upload any PDF on-the-fly. The system automatically extracts, chunks, and embeds its content.

Advanced RAG Pipeline: Leverages LangChain to orchestrate a sophisticated RAG pipeline, ensuring answers are accurate and contextually derived only from the document.

High-Quality Embeddings: Utilizes OpenAI's state-of-the-art embedding models for superior semantic understanding.

Efficient Vector Storage: Employs ChromaDB for fast, local, and persistent vector storage and retrieval.

Source Citing: Each answer is accompanied by excerpts from the source document, providing verification and context.

Secure & Private: API keys and sensitive data are managed securely using environment variables and are never exposed.

🛠️ Tech Stack & Architecture
This project uses a modern RAG architecture to provide a seamless question-answering experience.

Component	Technology	Purpose
Orchestration	LangChain	Glues all components together, manages chains and prompts.
LLM & Embeddings	OpenAI API (GPT-4, text-embedding-3-small)	Powers natural language understanding and response generation.
Vector Database	ChromaDB	Stores and retrieves text embeddings for fast semantic search.
Web Framework	Streamlit	Creates the interactive and real-time user interface.
PDF Processing	PyPDF2	Extracts text content from uploaded PDF files.
Environment Mgmt	python-dotenv	Manages API keys and configuration securely.
Architectural Diagram
text
User Query -> Streamlit UI -> LangChain Orchestrator
                                  |
            +---------------------+---------------------+
            |                                           |
    (1) Retriever -> ChromaDB (Vector Store)     (3) LLM (OpenAI GPT-4)
            |              ^                            |
            |              | (2)                        |
            +--------------+----------------------------+
                           |
                   (4) Final Answer -> Streamlit UI
Retrieval: The user's query is vectorized and used to retrieve relevant text chunks from ChromaDB.

Augmentation: The retrieved chunks are injected into a prompt template as context.

Generation: The augmented prompt is sent to the OpenAI LLM to generate a human-like answer.

Response: The final answer, along with its sources, is displayed in the UI.

🚀 Getting Started
Follow these steps to set up and run the project locally.

Prerequisites
Python 3.10+

An OpenAI API Key

1. Clone the Repository
bash
git clone https://github.com/your-username/pdf-insight-extractor.git
cd pdf-insight-extractor
2. Set Up a Virtual Environment
bash
# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Dependencies
bash
pip install -r requirements.txt
4. Configure Environment Variables
Create a .env file in the root directory and add your OpenAI API key:

text
# .env
OPENAI_API_KEY="your_openai_api_key_here"
ANONYMIZED_TELEMETRY=false
5. Run the Application
Launch the Streamlit app with the following command:

bash
streamlit run app.py
Navigate to http://localhost:8501 in your browser to start chatting with your PDFs!

💡 How to Use
Upload a PDF: Use the file uploader in the sidebar.

Process the PDF: Click the "Process PDF" button and wait for the system to embed the document.

Ask Questions: Type your questions into the chat input at the bottom of the screen and get instant, context-aware answers.

🔧 Future Enhancements
 Support for Multiple Documents: Extend the system to handle and query multiple PDFs simultaneously.

 Conversation Memory: Implement memory to allow follow-up questions and a more natural conversational flow.

 Dockerization: Containerize the application with Docker for easier deployment and scalability.

 Advanced Metadata Filtering: Allow users to filter searches by page number, section, or other metadata.

🤝 Contributing
Contributions are welcome! Please feel free to open an issue or submit a pull request to improve this project.

Fork the repository.

Create a new branch (git checkout -b feature/your-feature-name).

Make your changes and commit them (git commit -m 'Add some feature').

Push to the branch (git push origin feature/your-feature-name).

Open a Pull Request.

📄 License
This project is licensed under the MIT License. See the LICENSE file for details.