import openai
import os
from dotenv import load_dotenv

load_dotenv("./.env")

openai.api_key = os.environ["OPENAI_API_KEY"]

model = os.environ["MODEL"]

memory = [{"role": "system", 
             "content": "You are an Anime wifu named Chiaki Nanami from danganronpa. Respond in her lovely accent."}]

def chat(prompt):
    res = openai.ChatCompletion.create(
        model = model,
        messages = memory,
        temperature = 0.5
    )
    response_message = res.choices[0].message.content
    memory.append({"role": "assistant", "content": response_message}) 
    return memory

def main_chat(user):
    global memory
    memory.append({"role": "assistant", "content":user})
    return memory
if __name__ == "__main__":
    while True:
        user = input("User: ")
        print(chat(user))
        if user == "quit":
            break
        print(main_chat(user)[-1]["content"])