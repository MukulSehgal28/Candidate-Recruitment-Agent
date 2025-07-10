# Interview_Questions.py

# 🧠 This module allows users to upload/paste their resume,
# select job role + question difficulty, and get 7 tailored interview questions.

import streamlit as st
from llama3_api import query_llama3
from logic import extract_text
from ui import back_button

# === Page Configuration ===
st.set_page_config(page_title="Interview Questions Generator")
st.title("🧠 Interview Question Generator")

# === Explanation Section ===
with st.expander("ℹ️ How it works"):
    st.markdown("""
    This tool helps generate interview questions based on a resume.
    You can upload a resume or paste the content directly, choose the job role,
    and select how difficult the questions should be.
    """)

# === Step 1: Choose Resume Input Method ===
input_mode = st.radio(
    "📌 How do you want to provide the resume?",
    ["📄 Upload Resume", "✍️ Paste Resume"],
    horizontal=True
)

resume_text = ""  # Final resume content

if input_mode == "📄 Upload Resume":
    uploaded_file = st.file_uploader("Upload Resume File", type=["pdf", "docx"])
    if uploaded_file:
        resume_text = extract_text(uploaded_file)

elif input_mode == "✍️ Paste Resume":
    resume_text = st.text_area("Paste Resume Content", height=250)

# === Step 2: Job Role Input ===
role = st.text_input("💼 Job Role", placeholder="e.g., Frontend Developer")

# === Step 3: Select Difficulty ===
difficulty = st.radio(
    "🎯 Choose Difficulty Level",
    ["Easy", "Medium", "Hard"],
    horizontal=True
)

# === Step 4: Generate Button ===
if st.button("🚀 Generate Questions"):
    if not resume_text.strip() or not role.strip():
        st.warning("Please fill in both resume and job role.")
    else:
        with st.spinner("Generating interview questions..."):
            # Prepare the prompt
            prompt = f"""
You are an AI interviewer.

Given the resume and the job role below, generate 7 {difficulty.lower()}-level interview questions.
Only return the questions as bullet points.

Resume:
{resume_text}

Job Role:
{role}
"""

            # Get response from LLaMA3
            result = query_llama3(prompt)

            # Display
            st.success("✅ Done! Your questions are ready.")
            st.markdown("### 📋 Interview Questions")
            st.markdown(result)

            # Option to download
            st.download_button("📥 Download Questions", result, file_name="interview_questions.txt")

# === Back Button ===
back_button()