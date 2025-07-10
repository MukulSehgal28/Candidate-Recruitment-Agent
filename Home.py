# Home.py

# 📌 Import necessary module
import streamlit as st

# 🚀 Set up the basic configuration of the Streamlit web app
st.set_page_config(
    page_title="Candidate Recruitment Agent",  # Title shown on browser tab
    page_icon="🤖",                            # Icon on tab
    layout="wide",                             # Use full browser width
    initial_sidebar_state="expanded"           # Sidebar visible by default
)

# ====== MAIN HEADER SECTION ======
# Add a small logo or image at the top of the page
st.image("https://cdn-icons-png.flaticon.com/512/4712/4712109.png", width=80)

# Set the main title and short description
st.title("🤖 Candidate Recruitment Agent")
st.markdown("Smart Resume Analysis & Interview Preparation System")

# ====== MAIN NAVIGATION BUTTONS ======
# Organize buttons into columns for better layout
col1, col2, col3, col4 = st.columns(4)

# Each column contains a button to navigate to a different section
with col1:
    if st.button("📄 Analyze Resume"):
        # Navigate to the Analyze Resume page
        st.switch_page("pages/Analyze.py")

with col2:
    if st.button("💬 Resume Q&A"):
        # Navigate to the Resume Q&A module
        st.switch_page("pages/Resume_QA.py")

with col3:
    if st.button("🧠 Interview Questions"):
        # Navigate to the Interview Questions Generator
        st.switch_page("pages/Interview_Questions.py")

with col4:
    if st.button("🛠️ Resume Improvement"):
        # Navigate to the Resume Improvement tool
        st.switch_page("pages/Resume_Improvement.py")

# ====== SHORT FEATURE LIST ======
st.markdown("---")  # Divider line
st.subheader("📌 What this app does:")
st.markdown("""
- 🔍 **Analyze resumes** for job fit based on predefined or custom job descriptions  
- 💬 **Ask questions** to the AI about resume content  
- 🧠 **Generate interview questions** tailored to specific job roles  
- 🛠️ **Get improvement suggestions** to enhance your resume section-wise  
""")

# ====== ABOUT THE APP EXPANDER ======
# Show information about privacy and usage
with st.expander("🔐 About This App"):
    st.markdown("""
    - This application runs **entirely on your local machine**  
    - No resume data is uploaded to third-party servers  
    - Ideal for practice, portfolio review, or interview preparation  
    """)

# ====== FOOTER SECTION ======
# Add GitHub and contact info for credibility
st.markdown("🌐 [GitHub Repo](https://github.com)  |  📧 Contact: you@example.com")