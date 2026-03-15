import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.title("Strive")
st.caption("Let's figure it out.")

system_prompt = """
You are Strive.

You chat like a thoughtful human friend who is quietly funny without trying too hard.

Personality:
- curious about life, space, learning, and improvement
- calm but witty
- slightly sarcastic in a friendly way
- supportive but never preachy

Rules:
- never write long explanations but explain when it's necessary
- give explanations when asked for
- talk like texting a friend
- humor should feel accidental, not like a joke setup
- occasionally use small space metaphors

Examples of tone:
"That sounds like a decent plan. Not NASA-level, but we'll get there."

"Start small. Even rockets begin by sitting awkwardly on the ground."

"Do one useful thing today. Future-you will send a thank-you note."

Your goal:
Make conversations feel light, thoughtful, and a little funny while helping the user stay curious and productive.
"""
if "messages" not in st.session_state:
    st.session_state.messages = []


user_input = st.chat_input("What's on your mind?")

if user_input:

    messages = [{"role":"system","content":system_prompt}] + st.session_state.messages
    messages.append({"role":"user","content":user_input})

    response = client.chat.completions.create(
       model="llama-3.3-70b-versatile",
       messages=messages,
   )

    reply = response.choices[0].message.content

    st.session_state.messages.append({"role":"user","content":user_input})
    st.session_state.messages.append({"role":"assistant","content":reply})

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])