from typing import List
import openai
from openai import OpenAI
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
openai.api_key = os.getenv('OPENAI_API_KEY')
openai.base_url = "https://api.deepseek.com"

def get_completion(model: str, prompt: str, temperature: float = 0.0):
    messages = [
        {"role": "user", "content": prompt},
    ]
    response = openai.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message.content


def get_completion_from_messages(messages: List[str], model: str = "deepseek-chat", temperature: float = 0.0):
    response = openai.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message.content