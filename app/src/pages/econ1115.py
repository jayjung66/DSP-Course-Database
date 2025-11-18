import logging
logger = logging.getLogger(__name__)
import requests
import streamlit as st
from modules.nav import SideBarLinks

# Set the API base URL
API_BASE = "http://web-api:4000"

st.set_page_config(layout='wide')
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
with col1: st.metric("Average Enjoyment", "2.5/5", help="Based on student reviews")
with col2: st.metric("Average Difficulty", "2/5", help="Based on student reviews")
with col3: st.metric("Total Reviews", "2", help="Number of student reviews (ECON 1115 only)")
st.divider()

# -----------------------------------
# Professor Reviews
# -----------------------------------
st.subheader("👨‍🏫 Professor Reviews")
with st.expander("⭐ Professor: Peter Simon (2 reviews)", expanded=True):
    st.write("**Review - Susan Huang (Spring 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐ (2/5)")
    st.write("- **Difficulty:** 💪💪 (2/5)")
    st.info("**Comments:** No additional comments provided.")

    st.write("**Review - Abigail DeMaioribus (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐ (3/5)")
    st.write("- **Difficulty:** 💪💪 (2/5)")
    st.info("**Comments:** No additional comments provided.")
st.divider()

# -----------------------------------
# Key Takeaways
# -----------------------------------
st.subheader("💡 Key Takeaways from Reviews")
col1, col2 = st.columns(2)
with col1:
    st.write("**Most Popular Professors:**")
    st.write("1. Peter Simon (2 reviews)")
with col2:
    st.write("**Common Themes:**")
    st.write("- Moderate difficulty")
    st.write("- Mixed enjoyment ratings")
    st.write("- Introductory macroeconomics course")
st.divider()

# -----------------------------------
# Study Notes
# -----------------------------------
st.subheader("📂 Available Study Notes")
notes_list = [
    {"title": "Macroeconomics Midterm Study Guide", "file": "econ1115_midterm.pdf"},
    {"title": "Principles of Macroeconomics Notes", "file": "econ1115_notes.docx"},
    {"title": "Final Exam Review Sheet", "file": "econ1115_final.pdf"},
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
- 📘 [OpenStax Macroeconomics Textbook](#)  
- 🎓 [Khan Academy: Macroeconomics](https://www.khanacademy.org/)  
- 🎥 [YouTube Playlist: Principles of Macroeconomics](#)  
- 📊 [Practice Problems – Macroeconomic Models](#)  
""")
