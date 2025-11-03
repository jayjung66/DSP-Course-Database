import logging
logger = logging.getLogger(__name__)
import requests

import streamlit as st
from modules.nav import SideBarLinks

# Set the API base URL
API_BASE = "http://web-api:4000"

st.set_page_config(layout='wide')

# Sidebar
SideBarLinks()

# Back button
if st.button("⬅️ Back to Home"):
    st.switch_page('Home.py')

# -----------------------------------
# Page Content
# -----------------------------------
st.title("ECON 1115 – Principles of Macroeconomics")
st.write("Welcome, {0} 👋".format(st.session_state.get('first_name', 'Student')))
st.write("Here you can view professor rankings, notes, and useful resources for this course.")

st.divider()

# -----------------------------------
# Course Overview
# -----------------------------------
st.subheader("📊 Course Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Average Enjoyment", "2.5/5", help="Based on student reviews")

with col2:
    st.metric("Average Difficulty", "2/5", help="Based on student reviews")

with col3:
    st.metric("Total Reviews", "2", help="Number of student reviews")

st.divider()

# -----------------------------------
# Professor Information
# -----------------------------------
st.subheader("👨‍🏫 Professor: Peter Simon")

st.write("**Review #1 - Spring 2024:**")
st.write("- **Student:** Susan Huang")
st.write("- **Semester:** Spring 2024")
st.write("- **Format:** In Person")
st.write("- **Enjoyment Rating:** ⭐⭐ (2/5)")
st.write("- **Difficulty Rating:** 💪💪 (2/5)")

st.write("")

st.write("**Review #2 - Fall 2024:**")
st.write("- **Student:** Abigail DeMaioribus")
st.write("- **Semester:** Fall 2024")
st.write("- **Format:** In Person")
st.write("- **Enjoyment Rating:** ⭐⭐⭐ (3/5)")
st.write("- **Difficulty Rating:** 💪💪 (2/5)")

st.divider()

# -----------------------------------
# Student Comments & Advice
# -----------------------------------
st.subheader("💬 Student Comments & Advice")

with st.expander("📚 Review from Susan Huang (Spring 2024)", expanded=True):
    st.write("**Comments on Course:**")
    st.info("Check the course reviews for detailed feedback and experiences.")
    
    st.write("**Study Folder & Exam Advice:**")
    st.info("Students have contributed notes, past exams, and projects to help you succeed!")

with st.expander("📚 Review from Abigail DeMaioribus (Fall 2024)", expanded=False):
    st.write("**Comments on Course:**")
    st.info("Check the course reviews for detailed feedback and experiences.")
    
    st.write("**Study Folder & Exam Advice:**")
    st.info("Students have contributed notes, past exams, and projects to help you succeed!")

st.divider()

# -----------------------------------
# Study Notes
# -----------------------------------
st.subheader("📂 Available Study Notes")

notes_list = [
    {"title": "Macroeconomics Midterm Study Guide", "file": "macro_midterm_guide.pdf"},
    {"title": "GDP & National Income Notes", "file": "gdp_notes.docx"},
    {"title": "Fiscal Policy Summary", "file": "fiscal_policy.pdf"},
    {"title": "Final Exam Review Sheet", "file": "final_review.pdf"},
]

for note in notes_list:
    st.download_button(
        label=f"📄 {note['title']}",
        file_name=note['file'],
        data=f"Dummy content for {note['file']}",  # replace with actual file data
    )

st.divider()

# -----------------------------------
# Other Resources
# -----------------------------------
st.subheader("📖 Additional Resources")
st.markdown("""
- 📊 [Interactive Macroeconomic Models](#)  
- 🎥 [YouTube Playlist: ECON 1115 Explained](#)  
- 📘 [OpenStax Principles of Macroeconomics Textbook](https://openstax.org/books/principles-macroeconomics-2e/pages/1-introduction)  
- 🎓 [Khan Academy: Macroeconomics](https://www.khanacademy.org/economics-finance-domain/macroeconomics)
- 📈 [FRED Economic Data](https://fred.stlouisfed.org/)
""")