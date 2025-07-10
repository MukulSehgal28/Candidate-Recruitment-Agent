# llama3_api.py

import requests
import streamlit as st  # ✅ For reading secrets securely in Streamlit Cloud

# 🔐 Securely pull Groq API key from Streamlit Secrets
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

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