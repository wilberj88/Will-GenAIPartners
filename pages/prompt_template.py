import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate
import os

api_key1 = st.secrets["OPENAI_API_KEY"]

chat_model = ChatOpenAI(openai_api_key=api_key1)

template = "You area helpful assitant that translates {input_Language} to {output_Language}."
human_template = "{text}"

chat_prompt = ChatPromptTemplate.from_messages([
  ("system", template),
  ("human", human_template),
])

messages = chat_prompt.format_messages(input_Language="English",
                                       output_Language="French",
                                       text="I love programming recommender systems")

result = chat_model.predict_messages(messages)

st.write(result.content)
