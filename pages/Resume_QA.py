# Resume_QA.py

# 💬 This page lets users upload a resume and ask any question about it.
# LLaMA3 reads the resume and tries to answer based on the content.

import streamlit as st
from ui import qa_ui, back_button
from logic import extract_text
from llama3_api import query_llama3

# === Page Settings ===
st.set_page_config(page_title="Resume Q&A")
st.title("💬 Resume Q&A with AI")

st.markdown("Ask anything about your resume — education, skills, experience, etc. The AI will try to answer smartly based on the uploaded file.")

# === Upload resume & enter question ===
uploaded_file, question = qa_ui()

# === Ask button ===
if st.button("💬 Ask AI"):
    if not uploaded_file or not question.strip():
        st.warning("Please upload a resume and type a question.")
    else:
        with st.spinner("Reading resume and thinking..."):
            resume_text = extract_text(uploaded_file)

            if not resume_text:
                st.error("❌ Couldn't read text from the resume. Try another file.")
            else:
                # Send the question and resume content to LLaMA3
                prompt = f"""
You're a helpful assistant.

Here is a resume. Based on it, answer the following question from the user.

Question:
{question}

Resume:
{resume_text}
"""
                answer = query_llama3(prompt)

                st.success("✅ Answer Ready!")
                st.markdown("### 🤖 AI's Response")

                # Split long multi-question answers into bullets or slides
                lines = answer.split("\n")
                question_blocks = [line.strip("• ").strip() for line in lines if line.strip()]

                for idx, q in enumerate(question_blocks, 1):
                    with st.expander(f"📌 Q{idx}"):
                        st.write(q)

# === Back button to Home ===
back_button()
