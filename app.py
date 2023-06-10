import streamlit as st
import openai
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("openai.api_key")

start_sequence = "\nAI: "
restart_sequence = "\nHuman: "

st.title("Chatbot")
ask = st.text_input("Enter your message")

if st.button("Send"):
    if ask == "break":
        st.write("Thank you!")
    else:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=ask,
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=['Human :', "AI:"]
        )
        st.write("AI:", response['choices'][0]['text'])
