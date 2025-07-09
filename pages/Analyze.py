# Analyze.py

# 📄 This page allows users to compare their resume with a job description
# using either a pre-selected role or a custom JD. It then evaluates using LLaMA3.

import streamlit as st
from ui import resume_upload_ui, back_button
from logic import extract_text
from llama3_api import query_llama3

# 🧾 Page Setup
st.set_page_config(page_title="Resume Analyzer")
st.title("📄 Resume Analyzer")

st.markdown("Compare your resume against a specific job role or custom job description.")

# === 1. Choose how to provide the Job Description ===
jd_mode = st.radio(
    "📌 How would you like to provide the Job Description?",
    ["Select Job Role", "Upload/Paste Custom JD"],
    horizontal=True
)

# === 2. Pre-defined Job Roles ===
job_roles = {
    "Frontend Developer": "HTML, CSS, JavaScript, React, UI/UX, Webpack, REST APIs, Git",
    "Backend Developer": "Node.js, Express, Python, Django, REST APIs, SQL, MongoDB, Docker, Git",
    "AI/ML Engineer": "Python, PyTorch, TensorFlow, Machine Learning, MLOps, NLP, Hugging Face",
    "Data Scientist": "Python, Pandas, SQL, Data Viz, Machine Learning, Statistics, Cleaning",
    "DevOps Engineer": "CI/CD, Jenkins, Kubernetes, Docker, AWS, Linux, Terraform, Monitoring"
}

job_description = ""  # Final JD to send to LLaMA
selected_role = None

# === 3. Choose role or paste JD ===
if jd_mode == "Select Job Role":
    selected_role = st.selectbox("💼 Choose Job Role", list(job_roles.keys()))
    if selected_role:
        job_description = job_roles[selected_role]
        with st.expander(f"🔍 Skills Required for {selected_role}"):
            st.code(job_description.strip())
else:
    job_description = st.text_area(
        "✍️ Paste Your Own Job Description",
        placeholder="Type or paste the JD here...",
        height=200
    )

# === 4. Upload Resume ===
st.markdown("### 📄 Upload Your Resume File")
uploaded_file = st.file_uploader(
    "Supported formats: PDF, DOCX",
    type=["pdf", "docx"]
)

# === 5. Analyze Button ===
if st.button("🚀 Analyze Resume"):
    if not uploaded_file or not job_description.strip():
        st.warning("Please upload your resume and provide a job description.")
    else:
        with st.spinner("Analyzing your resume..."):
            resume_text = extract_text(uploaded_file)

            # Create LLaMA3 prompt
            prompt = f"""
You are an AI assistant helping in recruitment.

Compare this resume with the job description and give:
- Fit Score (0–10)
- 3 Strengths
- 2 Weaknesses or areas to improve
- A short one-line summary verdict

Job Description:
{job_description}

Resume:
{resume_text}
"""

            # Call LLaMA3 model
            result = query_llama3(prompt)

            # Show output
            st.success("✅ Analysis Complete!")
            st.markdown("### 🧠 AI's Evaluation")
            st.markdown(result)

            st.download_button("📥 Download Result", result, file_name="resume_analysis.txt")

# === 6. Back Button ===
back_button()
