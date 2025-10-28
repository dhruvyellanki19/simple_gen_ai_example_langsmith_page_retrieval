import os
from dotenv import load_dotenv

from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()


langchain_api_key = os.getenv("LANGCHAIN_API_KEY")
project_name = os.getenv("LANGCHAIN_PROJECT_NAME", "local_project")


if langchain_api_key:
    os.environ["LANGCHAIN_API_KEY"] = langchain_api_key
    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    os.environ["LANGCHAIN_PROJECT_NAME"] = project_name
else:
    st.warning("LANGCHAIN_API_KEY not found. Tracing will be disabled.")


st.title("🦙 Simple Retrieval GenAI Demo with LLaMA2 Model")


input_text = st.text_input("💭 What question do you have in mind?")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the question asked."),
    ("user", "Question: {question}")
])

llm = Ollama(model="llama2")
output_parser = StrOutputParser()

chain = prompt | llm | output_parser

if input_text:
    with st.spinner("Thinking..."):
        response = chain.invoke({"question": input_text})
    st.success("Response:")
    st.write(response)
