#LIBRARIES REQUIRED
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate
import os

#PAGE & TITLE CONFIG
st.title('Will`s home exercise')
st.header('For GenAI Partners')
st.write('Virtual Assistant For Onboarding in GenAI Partnerts')

#API CONECTIONS
api_key1 = st.secrets["OPENAI_API_KEY"]
#api_key2 = os.getenv("OPENAI_API_KEY")
chat_model = ChatOpenAI(openai_api_key=api_key1)

#USER INTERACTION
name = st.text_input("Please write your name:", key="new_talent_name")
rol = st.selectbox(
  "Please select your rol", 
  ("Machine Learning Engineer", "Artificial Intelligence Engineer", "Deep Learning Engineer"),
  index=None,
  placeholder="Select your new rol",
  key="new_talent_rol")
start = st.button("Start Onboarding Guide Process")
  
if start:
#ASSISTANT CONFIGURATION
    st.header("Welcome to GenAI Partners Team!")
    st.write(st.session_state.new_talent_name)
    st.write(st.session_state.new_talent_rol)
    template = """"
    You area helpful assistant for onboarding new talent in a company of generative artificial intelligence.
    The name of the company you work for is GenAI Partners.
    Your name as virtual assistant is Wilber and you are the host for the new ones.
    They will tell you their {name} and their {rol} and you will welcoming them and guide them.
    You have to guide the new talent to give 1) orientation, 2) precedents and  3) training for their new rol in the company.
    When you give orientation you explain the kind of mission and vision for a generative artificial intelligence company.
    When you give precedents you explain that the rol does
    When you give training you select the top 5 books about the rol
    Then you tell the new talent that the day for star working is thursday january 18 of 2024.
    Finally ask by the name of the new talent if he o she has questions about the process and if they have all the tests done to start the job. 
    """
    human_template = "{st.session_state.new_talent_name}, {st.session_state.new_talent_rol}"
  
    chat_prompt = ChatPromptTemplate.from_messages([
      ("system", template),
      ("human", human_template),
    ])
  
    messages = chat_prompt.format_messages(name={st.session_state.new_talent_name},
                                           rol = {st.session_state.new_talent_rol},
                                           )
    
    result = chat_model.predict_messages(messages)

#ASSISTANT GENERATIVE RESPONSE
    st.write(result.content)
