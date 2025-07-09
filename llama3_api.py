# llama3_api.py

# 🔗 Handles connection to Groq's LLaMA3 API for generating AI responses.

import os
import requests
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def call_llama3(prompt):
    """
    Sends a prompt to LLaMA3 via Groq API and returns the response.
    """
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama3-70b-8192",
        "messages": [
            {"role": "system", "content": "You are a helpful AI recruitment assistant."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.4
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"❌ API Error: {str(e)}"

def query_llama3(prompt):
    """
    A cleaner helper to call LLaMA3.
    """
    return call_llama3(prompt)
