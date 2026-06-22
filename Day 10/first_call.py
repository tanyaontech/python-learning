#pip intsall groq
from groq import Groq
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
api_key = os.environ.get("GROQ_API_KEY")
client= Groq(api_key=api_key)
response = client.chat.completions.create(
    model ="openai/gpt-oss-120b",
    messages=[
        {"role":"system",
        "content":"You are a helpfull assistant"
        },
        {"role":"user",
         "content":"Explain what is an API in 1 line"}
    ]
)
print(response.choices[0].message.content)