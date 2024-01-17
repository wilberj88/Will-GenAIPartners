#LIBRARIES REQUIRED
import streamlit as st
from langchain.chat_models import ChatOpenAI
import os
from st_pages import Page, show_pages, add_page_title

# Optional -- adds the title and icon to the current page
add_page_title()

# Specify what pages should be shown in the sidebar, and what their titles and icons
# should be
show_pages(
    [
        Page("home.py", "Home", "🏠"),
        Page("pages/simple.py", "Page 2", ":books:"),
        Page("pages/prompt_template.py", "Page 3", ":books:"),
        Page("pages/home_exercise.py", "Page 4", ":books:"),
    ]
)


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
st.subheader('3 different implementations of Personalized Guide by Generative Virtual Assistant')
st.write('Look the 3 tries in the pages of the left 👈')
st.write('The simpliest one is <simple>, the next takes multiple parameters <prompt template> and the most complex is in <home exercise>')
