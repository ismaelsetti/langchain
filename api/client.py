import requests
import streamlit as st


def get_openai_response(input_text):
    response = requests.post(
        url="http://localhost:8000/essay/invoke",
        json={"input": {"topic": input_text}}
    )
    return response.json()['output']['content']


def get_ollama_response(input_text):
    response = requests.post(
        url="http://localhost:8000/poem/invoke",
        json={"input": {"topic": input_text}}
    )
    return response.json()['output']


st.title("Langchain Demo")
input_text1 = st.text_input("Write an essay with OpenAI about")
input_text2 = st.text_input("Write a poem with LLama2 about")

if input_text1:
    st.write(get_openai_response(input_text1))

if input_text2:
    st.write(get_ollama_response(input_text2))
