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
st.header("By Wilber Jiménez Hernández at january 17/2024")
st.divider()
st.title('Personalized Guide by Generative Virtual Assistant')

#INPUTS
#input_name = st.text_input("Please write your name:")
input_rol = st.selectbox(
  'Plase select your rol for a personalized onboarding guide', 
  rol, 
  index=None,
  placeholder="Choose an option")


#PROMPT
prompt = "Hi I am new employee as in GenAI Partnerts Consultants, please guide me in the process to understand how a generative artificial intelligence company works and what a {input_rol} does, also give me tips for orientation, precedents and training for my new rol"
with st.expander("See the prompt for this use case"):
  st.write(prompt)
st.divider()


#SHOW BOTs MESSAGES
st.write('Virtual Assistant 🤖 says:')
result = chat_model.predict(prompt)
if input_rol:
  st.write(result)
