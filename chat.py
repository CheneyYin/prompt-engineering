import openai
from openai import OpenAI
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
openai.api_key = os.getenv('OPENAI_API_KEY')
openai.base_url = "https://api.deepseek.com"

def get_completion(model: str, prompt):
    messages = [
        {"role": "user", "content": prompt},
    ]
    response = openai.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message.content

print(get_completion("deepseek-chat", "列举三首李白的诗"))
print(get_completion("deepseek-chat", "这三首诗，你最欣赏哪一首？为什么？"))