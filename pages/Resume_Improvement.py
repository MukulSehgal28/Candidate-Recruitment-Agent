# Resume_Improvement.py

# 🛠️ This page allows users to upload their resume and choose areas they'd like to improve.
# The AI gives helpful tips based on the selected sections.

import streamlit as st
from logic import extract_text
from llama3_api import query_llama3
from ui import back_button

# === Page Setup ===
st.set_page_config(page_title="Resume Improvement")
st.title("🛠️ Resume Improvement Assistant")

# === Instructions for Users ===
with st.expander("ℹ️ How it works"):
    st.markdown("""
    Want to improve your resume? Just upload it and select the parts you'd like help with —
    like content, format, or skills. The AI will give you specific suggestions to enhance it.
    """)

# === Step 1: Upload Resume ===
uploaded_file = st.file_uploader("📄 Upload Your Resume (PDF or DOCX)", type=["pdf", "docx"])
resume_text = ""

if uploaded_file:
    resume_text = extract_text(uploaded_file)

# === Step 2: Select Areas to Improve ===
st.markdown("### 🎯 What would you like to improve?")
improvement_areas = st.multiselect(
    "Choose one or more sections:",
    [
        "Content",
        "Skills Highlighting",
        "Format",
        "Experience Description",
        "Education",
        "Projects",
        "Achievements",
        "Overall Structure"
    ]
)

# === Step 3: Generate Suggestions ===
if st.button("🚀 Improve My Resume"):
    if not resume_text or not improvement_areas:
        st.warning("Please upload your resume and select at least one improvement area.")
    else:
        with st.spinner("Analyzing resume and writing suggestions..."):
            # Prepare prompt for LLaMA3
            prompt = f"""
You're an AI resume coach.

Here is a candidate's resume. Suggest improvements only for the following areas:
{', '.join(improvement_areas)}.

Resume:
{resume_text}

Return tips and suggestions as bullet points, organized by section.
"""
            # Call LLaMA3 API
            result = query_llama3(prompt)

            # Show results
            st.success("✅ Done! See your suggestions below.")
            st.markdown("### ✨ Suggestions for Improvement")
            st.markdown(result)

            st.download_button("📥 Download Suggestions", result, file_name="resume_improvement.txt")

# === Step 4: Back to Home Button ===
back_button()