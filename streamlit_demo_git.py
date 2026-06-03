import os

import streamlit as st
from langchain_openai import ChatOpenAI

st.title("Ask Anything")

with st.sidebar:
    st.title("Provide your API Key")
    OPENAI_API_KEY = st.text_input("OpenAI API Key", type="password")
if not OPENAI_API_KEY:
    st.info("Please provide your OpenAI API Key to Continue...")
    st.stop()

llm = ChatOpenAI(model= "gpt-4o-mini", api_key=OPENAI_API_KEY)

question =  st.text_input("Enter your question")

if question:
    response = llm.invoke(question)
    st.write(response.content)