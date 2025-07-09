# ui.py

# 📌 This file contains reusable UI components like file upload blocks, input forms,
# navigation sidebar, and a back button — all used in multiple pages of the app.

import streamlit as st


def resume_upload_ui():
    """
    📄 Section for uploading a resume and entering a job description.
    Used in the Resume Analysis module.
    
    Returns:
        uploaded_file (UploadedFile): The uploaded resume file
        job_description (str): The job description text entered by user
    """
    st.markdown("### 📄 Upload Resume and Enter Job Description")
    
    # File uploader: accepts only PDF and DOCX formats
    uploaded_file = st.file_uploader(
        "Upload Resume (PDF or DOCX)", 
        type=["pdf", "docx"]
    )

    # Text area for the user to paste or type the job description
    job_description = st.text_area(
        "💼 Enter Job Description", 
        height=200,
        placeholder="e.g., We’re looking for a frontend developer skilled in React, JavaScript, and UI design..."
    )

    return uploaded_file, job_description


def qa_ui():
    """
    💬 Section to upload a resume and ask a free-text question about it.
    Used in the Resume Q&A module.

    Returns:
        uploaded_file (UploadedFile): Resume file
        question (str): User's question input
    """
    st.markdown("### 💬 Resume Q&A")

    # File upload (key used to avoid conflict with other uploaders)
    uploaded_file = st.file_uploader(
        "Upload Resume (PDF or DOCX)", 
        type=["pdf", "docx"], 
        key="qa_file"
    )

    # User types the question to ask about the resume
    question = st.text_input(
        "Ask a question about the resume",
        placeholder="e.g., What are the candidate’s main strengths?"
    )

    return uploaded_file, question


def back_button():
    """
    🔙 Back button to return to the Home page.
    Placed at the bottom of most modules.
    """
    if st.button("🔙 Back to Home"):
        st.switch_page("Home.py")


def show_sidebar():
    """
    📍 Sidebar for navigation across different sections of the app.
    Includes branding, navigation radio, and basic app info.
    
    Returns:
        menu (str): The selected menu option (used for routing if needed)
    """
    with st.sidebar:
        # Branding icon/logo
        st.image("https://cdn-icons-png.flaticon.com/512/4712/4712109.png", width=80)

        # App title
        st.title("🚀 Euron Recruitment Agent")
        st.markdown("AI-Powered Resume Analysis & Interview Prep")

        # Radio buttons for navigation
        menu = st.radio(
            "📍 Navigate to:",
            [
                "🏠 Home",
                "📄 Resume Analysis",
                "📄 Resume Q&A",
                "🧠 Interview Questions",
                "🛠️ Resume Improvement"
            ],
            label_visibility="visible"
        )

        # Divider and info
        st.markdown("---")

        # About the app (optional)
        with st.expander("🔐 About This App"):
            st.markdown("""
            - This app runs **locally on your machine**
            - Resume files and user data are **not shared with external servers**
            - Built using **Python + Streamlit** by a beginner for learning purposes
            """)

        # Footer with GitHub and email
        st.markdown("🌐 [GitHub Repo](https://github.com)  |  📧 Contact: you@example.com")

    return menu