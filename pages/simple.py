#LIBRARIES REQUIRED
import streamlit as st
from langchain.chat_models import ChatOpenAI
import os

#API CONNECTION
api_key1 = st.secrets["OPENAI_API_KEY"]
#api_key2 = os.getenv("OPENAI_API_KEY") #In case you want to try the code in local

#LANGCHAIN MODEL
chat_model = ChatOpenAI(openai_api_key=api_key1)

#PROMPT
result = chat_model.predict("Hi my name is Wilber and I am new employee as in GenAI Partnerts Consultants, please guide me in the process to understand how a generative artificial intelligence company works and what a machine learning engineer does, also give me tips for orientation, precedents and training for my new rol")

#TITLE AND PERSONALIZED RESULTS
st.title('Personalized Guide by Generative Virtual Assistant')
st.header('Example with me and my rol in GenAI Parters')
with st.expander("See the prompt"):
  st.write("Hi my name is Wilber and I am new employee as in GenAI Partnerts Consultants, please guide me in the process to understand how a generative artificial intelligence company works and what a machine learning engineer does, also give me tips for orientation, precedents and training for my new rol")
st.divider()
st.write(result)
