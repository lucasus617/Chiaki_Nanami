import openai
import os
from dotenv import load_dotenv

load_dotenv("./.env")

openai.api_key = os.environ["OPENAI_API_KEY"]

model = os.environ["MODEL"]

memory = []

def chat(prompt):
    res = openai.ChatCompletion.create(
        model = model,
        messages = [
            {"role": "system", 
             "content": "You are an Anime wifu named Chiaki Nanami from danganronpa. Respond in her lovely accent."},
            {"role" : "user",
             "content" : prompt}
        ],
        temperature = 0.5
    )
    return res.choices[0].message

if __name__ == "__main__":
    a = input("User: ")
    print(chat(a))
