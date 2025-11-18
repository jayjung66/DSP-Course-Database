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
st.title("CRIM 1120 – Criminology")
st.write("Welcome, {0} 👋".format(st.session_state.get('first_name', 'Student')))
st.write("Here you can view professor rankings, notes, and useful resources for this course.")
st.divider()

# -----------------------------------
# Course Overview
# -----------------------------------
st.subheader("📊 Course Overview")
col1, col2, col3 = st.columns(3)
with col1: st.metric("Average Enjoyment", "4/5", help="Based on student reviews")
with col2: st.metric("Average Difficulty", "2/5", help="Based on student reviews")
with col3: st.metric("Total Reviews", "1", help="Number of student reviews (CRIM 1120 only)")
st.divider()

# -----------------------------------
# Professor Reviews
# -----------------------------------
st.subheader("👨‍🏫 Professor Reviews")
with st.expander("⭐ Professor: Norair Khachatryan (1 review)", expanded=True):
    st.write("**Review - Rachel Song (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐⭐ (4/5)")
    st.write("- **Difficulty:** 💪💪 (2/5)")
    st.info("**Comments:** No additional comments provided.")
st.divider()

# -----------------------------------
# Key Takeaways
# -----------------------------------
st.subheader("💡 Key Takeaways from Reviews")
col1, col2 = st.columns(2)
with col1: st.write("**Most Popular Professors:**\n1. Norair Khachatryan (1 review)")
with col2: st.write("**Common Themes:**\n- Moderate difficulty\n- High enjoyment\n- Introductory criminology course")
st.divider()

# -----------------------------------
# Study Notes
# -----------------------------------
st.subheader("📂 Available Study Notes")
notes_list = [
    {"title": "Criminology Midterm Study Guide", "file": "crim1120_midterm.pdf"},
    {"title": "Theories of Crime Notes", "file": "crim1120_theories.docx"},
    {"title": "Final Exam Review Sheet", "file": "crim1120_final.pdf"},
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
- 📘 [OpenStax Criminology Textbook](#)  
- 🎓 [Khan Academy: Sociology & Crime](https://www.khanacademy.org/)  
- 🎥 [YouTube Playlist: Intro to Criminology](#)  
- 📊 [Criminology Research Resources](#)  
""")
