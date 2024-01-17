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


#TITLE 
st.title("Exercise for GenAI Partners")
st.header("By Wilber Jiménez Hernández")
st.divider()
st.title('Personalized Guide by Generative Virtual Assistant')
st.header('Please select your rol an receive a personalized onboarding guide')

#INPUTS
input_name = st.text_input("Please write your name:")
input_rol = st.selectbox('Plase select your rol', rol, key = 'rol_de_entrada')


#PROMPT
with st.expander("See the prompt"):
  st.write("Hi my name is (name_typed) and I am new employee as in GenAI Partnerts Consultants, please guide me in the process to understand how a generative artificial intelligence company works and what a (rol_selected) does, also give me tips for orientation, precedents and training for my new rol")
st.divider()
st.write('Virtual Assistant 🤖 says:')

#SHOW BOTs MESSAGES
result = chat_model.predict("Hi my name is {input_name} and I am new employee as in GenAI Partnerts Consultants, please guide me in the process to understand how a generative artificial intelligence company works and what a {input_rol} does, also give me tips for orientation, precedents and training for my new rol")
st.write(result)
