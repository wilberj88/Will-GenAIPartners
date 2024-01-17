#LIBRARIES REQUIRED
import streamlit as st
from langchain.chat_models import ChatOpenAI
import os

#API CONNECTION
api_key1 = st.secrets["OPENAI_API_KEY"]
#api_key2 = os.getenv("OPENAI_API_KEY") #In case you want to try the code in local

#LANGCHAIN MODEL
chat_model = ChatOpenAI(openai_api_key=api_key1)

#OPTIONS RETRIEVAL AUGMENTED 
rol = ['Machine learning Engineer', 'Artificial Intelligence Engineer', 'Data Scientist']


#PAGE AND TITLE CONFIG
st.set_page_config(
    layout = 'wide',
    page_title = 'Wilber Test for GenAI Partners')

st.title("Exercise for GenAI Partners")
st.header("By Wilber Jiménez Hernández at january 17/2024")
st.divider()
st.title('3 differents implementation of Personalized Guide by Generative Virtual Assistant')
