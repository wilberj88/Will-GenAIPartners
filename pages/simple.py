import streamlit as st
from langchain.chat_models import ChatOpenAI
import os


api_key1 = st.secrets["OPENAI_API_KEY"]

api_key2 = os.getenv("OPENAI_API_KEY")

chat_model = ChatOpenAI(openai_api_key=api_key1)

result = chat_model.predict("Hi my name is Wilber and I am new employee as in GenAI Partnerts Consultants, please guide me in the process to understand how a generative artificial intelligence company works and what a machine learning engineer does, also give me tips for orientation, precedents and training for my new rol")

st.title('Guide by Virtual Assistant')
st.header('Personalized by my name, rol and kind of company (GenAI Partners)')
with st.expander("See the prompt:")
  st.write("Hi my name is Wilber and I am new employee as in GenAI Partnerts Consultants, please guide me in the process to understand how a generative artificial intelligence company works and what a machine learning engineer does, also give me tips for orientation, precedents and training for my new rol")
st.divider()
st.write(result)
