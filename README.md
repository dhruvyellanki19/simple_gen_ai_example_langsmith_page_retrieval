# LangChain RAG Example

A simple project to learn and practice RAG (Retrieval-Augmented Generation) with LangChain.

## � Streamlit Web App

The project includes a user-friendly Streamlit web interface (`app.py`) that provides:
- Interactive document upload (PDF files or web URLs)
- Real-time document processing and vector store creation
- Question-answering interface with context display
- FAISS-powered similarity search for efficient retrieval

**Note:** This app runs locally only because it uses Ollama with Llama2 model, which requires local installation and cannot be deployed to cloud platforms without significant configuration.

## What it does

Loads a webpage → Splits text → Creates embeddings → Stores in vector DB → Retrieves relevant context → Uses LLM to generate answers

## Setup

1. Install Ollama and pull llama2:
   ```bash
   ollama pull llama2
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create `.env` file:
   ```env
   LANGCHAIN_API_KEY=your_key_here
   LANGCHAIN_PROJECT_NAME=your_project_name
   ```

## Usage

### Streamlit Web Interface
```bash
streamlit run app.py
```
This launches an interactive web app where you can:
1. Upload PDF documents or provide web URLs
2. Watch as the system processes documents and creates vector embeddings
3. Ask questions and receive answers with source context
4. View retrieved document chunks for transparency

### Jupyter Notebook
Run the Jupyter notebook `app.ipynb` cell by cell to see the complete RAG pipeline in action.

## What you'll learn

- How RAG works step by step
- LangChain document processing
- Vector embeddings and similarity search
- Connecting retrieval with LLM generation

## Tech Stack

- **LangChain** - RAG framework
- **FAISS** - Vector database  
- **Ollama** - Local LLM (Llama2)
- **Streamlit** - Web interface
- **Jupyter** - Interactive development
- **LangSmith** - Tracing and monitoring

## Features

- 📄 **Document Processing** - Upload PDFs or provide URLs through web interface
- 🔍 **Smart Search** - FAISS-powered vector similarity search for efficient retrieval
- 🤖 **Local LLM** - Powered by locally installed Ollama Llama2 model
- 📊 **Context Display** - View retrieved document chunks for answer transparency
- 🔧 **LangSmith Integration** - Full tracing and monitoring capabilities
- 💻 **Local Development** - Runs entirely on your machine with no cloud dependencies

## Why Not Deployed?

This app uses Ollama with the Llama2 model running locally on your machine. Cloud deployment would require:
- Significant infrastructure costs for GPU-powered instances
- Complex model hosting setup
- Or switching to cloud-based LLM APIs (OpenAI, Anthropic, etc.)

The current setup demonstrates how to build a Simple starter RAG system for beginners using free, locally-running models.