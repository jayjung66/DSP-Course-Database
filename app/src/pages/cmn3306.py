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
st.title("CMN 3360 – Crisis Communication")
st.write("Welcome, {0} 👋".format(st.session_state.get('first_name', 'Student')))
st.write("Here you can view professor rankings, notes, and useful resources for this course.")

st.divider()

# -----------------------------------
# Course Overview
# -----------------------------------
st.subheader("📊 Course Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Average Enjoyment", "2/5", help="Based on student reviews")

with col2:
    st.metric("Average Difficulty", "2/5", help="Based on student reviews")

with col3:
    st.metric("Total Reviews", "1", help="Number of student reviews (CMN 3360 only)")

st.divider()

# -----------------------------------
# Professor Reviews
# -----------------------------------
st.subheader("👨‍🏫 Professor Reviews")

# Professor: Rosanna Fiske (1 review)
with st.expander("⭐ Professor: Rosanna Fiske (1 review)", expanded=True):
    st.write("**Review - Ty Orlando (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐ (2/5)")
    st.write("- **Difficulty:** 💪💪 (2/5)")

st.divider()

# -----------------------------------
# Key Takeaways
# -----------------------------------
st.subheader("💡 Key Takeaways from Reviews")

col1, col2 = st.columns(2)

with col1:
    st.write("**Most Popular Professors:**")
    st.write("1. Rosanna Fiske (1 review)")

with col2:
    st.write("**Common Themes:**")
    st.write("- Moderate difficulty")
    st.write("- Lower enjoyment rating")
    st.write("- Limited review data available")

st.divider()

# -----------------------------------
# Study Notes
# -----------------------------------
st.subheader("📂 Available Study Notes")

notes_list = [
    {"title": "Crisis Communication Case Studies", "file": "crisis_cases.pdf"},
    {"title": "Strategies & Frameworks Notes", "file": "crisis_strategies.docx"},
    {"title": "Midterm Study Guide", "file": "cmn3360_midterm.pdf"},
    {"title": "Final Exam Review Sheet", "file": "cmn3360_final_review.pdf"},
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
- 📘 [Institute for Public Relations – Crisis Communication](https://instituteforpr.org/crisis-communication/)  
- 🎓 [Khan Academy: Communication Basics](https://www.khanacademy.org/)  
- 🎥 [YouTube Playlist: Crisis Communication Explained](#)  
- 💼 [Harvard Business Review – Crisis Management Articles](https://hbr.org/)  
""")
