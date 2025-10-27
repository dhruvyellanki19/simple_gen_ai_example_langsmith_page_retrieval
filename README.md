# LangChain RAG Example

A simple project to learn and practice RAG (Retrieval-Augmented Generation) with LangChain.

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

Run the Jupyter notebook `app.ipynb` cell by cell to see the complete RAG pipeline in action.

## What you'll learn

- How RAG works step by step
- LangChain document processing
- Vector embeddings and similarity search
- Connecting retrieval with LLM generation

## Tech Stack

- LangChain - RAG framework
- FAISS - Vector database
- Ollama - Local LLM (Llama2)
- Jupyter - Interactive development