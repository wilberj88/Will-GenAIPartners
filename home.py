#LIBRARIES REQUIRED
import streamlit as st
from langchain.chat_models import ChatOpenAI
import os
from streamlit_option_menu import option_menu

# 1. as sidebar menu
with st.sidebar:
    selected = option_menu("Main Menu", ["Home", 'Simpliest try 1', 'Second simpliest try 2', 'Third try of the day'], 
        icons=['house', 'gear', 'house'], menu_icon="cast", default_index=1)
    selected




#API CONNECTION
api_key1 = st.secrets["OPENAI_API_KEY"]
#api_key2 = os.getenv("OPENAI_API_KEY") #In case you want to try the code in local

#LANGCHAIN MODEL
chat_model = ChatOpenAI(openai_api_key=api_key1)

#OPTIONS RETRIEVAL AUGMENTED 
rol = ['Machine learning Engineer', 'Artificial Intelligence Engineer', 'Data Scientist']




st.title("Exercise for GenAI Partners")
st.header("By Wilber Jiménez Hernández at january 17/2024")
st.divider()
st.subheader('3 different implementations of Personalized Guide by Generative Virtual Assistant')
st.write('Look the 3 tries in the pages of the left 👈')
st.write('The simpliest one is <simple>, the next takes multiple parameters <prompt template> and the most complex is in <home exercise>')
