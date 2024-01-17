#LIBRARIES REQUIRED
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate
import os


#PAGE & TITLE CONFIG
st.title('Will`s home exercise')
st.header('For GenAI Partners')
st.write('Virtual Assistant For Onboarding in GenAI Partnerts')
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate
import os

api_key1 = st.secrets["OPENAI_API_KEY"]

chat_model = ChatOpenAI(openai_api_key=api_key1)

template = """"
    You area helpful assistant for onboarding new talent in a company of generative artificial intelligence.
    The name of the company you work for is GenAI Partners.
    Your name as virtual assistant is R2D2 and you are the host for the new ones.
    They will tell you their {user_name} and their {user_rol} and you will welcoming them and guide them.
    You have to guide the new talent to give 1) orientation, 2) precedents and  3) training for their new rol in the company.
    When you give orientation you explain the kind of mission and vision for a generative artificial intelligence company.
    When you give precedents you explain that the rol does
    When you give training you select the top 5 books about the rol
    You have to write the orientation, precedents and training in steps.
    Then you tell the new talent that the day for star working is thursday january 18 of 2024.
    Finally ask by the name of the new talent if he o she has questions about the process and if they have all the tests done to start the job. 
    """

human_template = "{text}"

chat_prompt = ChatPromptTemplate.from_messages([
  ("system", template),
  ("human", human_template),
])

input_user_name = st.text_input("Please write your name:")
rol = ['Machine learning Engineer', 'Artificial Intelligence Engineer', 'Data Scientist']
input_user_rol = st.selectbox(
  'Please select your rol for a personalized onboarding guide', 
  rol, 
  index=None,
  placeholder="Choose an option")

messages = chat_prompt.format_messages(user_name="{input_user_name}",
                                       user_rol="{input_user_rol}",
                                       text="Please give me my personalized onboarding guide to the company")

result = chat_model.predict_messages(messages)

st.write(result.content)



prompt = st.chat_input("Say something")

if prompt:
    st.write(f"User has sent the following prompt: {prompt}")
