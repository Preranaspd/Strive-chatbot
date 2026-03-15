import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

messages = []

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chat ended")
        break

    messages.append({
        "role": "user",
        "content": user_input
    })

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )

    reply = response.choices[0].message.content

    messages.append({
        "role": "assistant",
        "content": reply
    })

    print("Bot:", reply)