import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

#completion = client.chat.completions.create(
#    model="gpt-4.5-preview",
#    messages=[
#        {
#            "role": "user",
#            "content": "G'day mate"
#        }
#    ]
#)
#print(completion.choices[0].message.content)

# Initialize the chat history
chat_history = []
while True:
    prompt = input("> ")
    if prompt == "exit":
        exit()
    # Add the user message to the chat history
    chat_history.append({
        "role": "user",
        "content": prompt,
    })
    # Send the full chat history
    completion = client.chat.completions.create(
        model="gpt-4.5-preview", messages=chat_history
    )
    # Display the answer
    answer = completion.choices[0].message.content
    print(answer)
    # Add the answer to the chat history
    chat_history.append({
        "role": "assistant",
        "content": answer,
    })