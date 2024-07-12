import streamlit as st 
import os 
import string

def ai():
    from groq import Groq
    client=Groq(
        api_key=GROQ_API_KEY,
    )
    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content":user_input,
        }
    ],
    model="llama3-70b-8192",)  
    st.write("GROQ:")
    st.write(chat_completion.choices[0].message.content)

st.title("MINEY🎭👨‍🎤🎬")
input = st.text_input("Enter your question")
character=st.text_input("Enter the characther that has to answer👨‍🎤:\t")
user_input=input+character

GROQ_API_KEY=st.text_input("Enter You API Key:")

# Display the user input
st.write('The user entered:', user_input)
st.write(ai())
