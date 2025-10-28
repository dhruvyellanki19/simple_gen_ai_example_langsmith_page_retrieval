# LangChain RAG Starter for Beginners

A simple learning project to understand **RAG (Retrieval-Augmented Generation)** concepts using LangChain. Perfect for beginners who want to learn how AI systems can retrieve information from documents and generate intelligent responses.

## What is this project?

This is a **beginner-friendly starter project** that demonstrates:

1. **Basic LangChain concepts** - How to chain prompts, models, and parsers
2. **Local AI models** - Using Ollama with LLaMA2 (runs on your computer)
3. **Document retrieval** - How to load, process, and search through documents
4. **Simple web interface** - Interactive Streamlit app to test your AI system

## What's included?

### `app.py` - Simple Q&A Interface
- Basic Streamlit web app with a text input
- Connects to locally running LLaMA2 model via Ollama
- Shows how to build a simple LangChain pipeline: `prompt | llm | output_parser`
- Optional LangSmith tracing to see what happens behind the scenes

### `app.ipynb` - Full RAG Learning Tutorial  
- Step-by-step Jupyter notebook showing complete RAG workflow
- Loads a webpage (LangSmith documentation)
- Splits text into chunks for processing
- Creates vector embeddings and stores them in FAISS
- Retrieves relevant information to answer questions
- Perfect for learning each step of the RAG process

## How to get started?

### 1. Install Ollama and download LLaMA2
```bash
# Install Ollama from https://ollama.ai
ollama pull llama2
```

### 2. Install Python dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up environment variables (optional)
Create a `.env` file:
```
LANGCHAIN_API_KEY=your_langsmith_key_here
LANGCHAIN_PROJECT_NAME=my_rag_learning_project
```

### 4. Try the simple app
```bash
streamlit run app.py
```

### 5. Learn with the notebook
```bash
jupyter notebook app.ipynb
```

## What will you learn?

- **How RAG works**: Load documents → Split into chunks → Create embeddings → Store in vector database → Retrieve relevant chunks → Generate answers
- **LangChain basics**: Prompts, models, output parsers, and chains
- **Vector search**: How computers find similar text using embeddings
- **Local AI**: Running powerful models on your own computer
- **Document processing**: How to prepare text data for AI systems
- **LangSmith tracking**: How to monitor and debug your AI chains in real-time

## LangSmith Tracking & Monitoring

This project includes **LangSmith integration** for tracking your AI chains:

**What is LangSmith?**
- A platform for monitoring, debugging, and improving LangChain applications
- Shows you exactly what happens in each step of your AI pipeline
- Helps you understand token usage, response times, and errors

**How it works in this project:**
- When you set `LANGCHAIN_API_KEY`, every question and response gets tracked
- You can see the full conversation flow in the LangSmith dashboard
- Perfect for learning how your prompts and chains actually work

**To enable tracking:**
1. Sign up at [smith.langchain.com](https://smith.langchain.com)
2. Get your API key and add it to `.env`
3. Run the app and see your traces in the dashboard

This is especially helpful for beginners to understand what's happening "under the hood" of their AI applications!

## Why start here?

- **No cloud costs** - Everything runs locally
- **Step-by-step learning** - From simple Q&A to full RAG system
- **Real examples** - Working code you can modify and experiment with
- **Foundation building** - Core concepts you'll use in advanced projects

## Next steps after this project

Once you understand the basics, you can:
- Add more document types (PDFs, websites, databases)
- Try different embedding models
- Experiment with different LLMs
- Build more complex retrieval strategies
- Create production-ready applications

Happy learning! 🚀

