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
st.title("ECON 1260 – Contested Issues in the U.S. Economy")
st.write("Welcome, {0} 👋".format(st.session_state.get('first_name', 'Student')))
st.write("Here you can view professor rankings, notes, and useful resources for this course.")
st.divider()

# -----------------------------------
# Course Overview
# -----------------------------------
st.subheader("📊 Course Overview")
col1, col2, col3 = st.columns(3)
with col1: st.metric("Average Enjoyment", "4/5", help="Based on student reviews")
with col2: st.metric("Average Difficulty", "1/5", help="Based on student reviews")
with col3: st.metric("Total Reviews", "1", help="Number of student reviews (ECON 1260 only)")
st.divider()

# -----------------------------------
# Professor Reviews
# -----------------------------------
st.subheader("👨‍🏫 Professor Reviews")
with st.expander("⭐ Professor: Peter Simon (1 review)", expanded=True):
    st.write("**Review - Amy Park (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐⭐ (4/5)")
    st.write("- **Difficulty:** 💪 (1/5)")
    st.info("**Comments:** No additional comments provided.")
st.divider()

# -----------------------------------
# Key Takeaways
# -----------------------------------
st.subheader("💡 Key Takeaways from Reviews")
col1, col2 = st.columns(2)
with col1: st.write("**Most Popular Professors:**\n1. Peter Simon (1 review)")
with col2: st.write("**Common Themes:**\n- Very easy workload\n- High enjoyment\n- Focus on economic debates and contested issues")
st.divider()

# -----------------------------------
# Study Notes
# -----------------------------------
st.subheader("📂 Available Study Notes")
notes_list = [
    {"title": "Contested Issues Reading Guide", "file": "econ1260_readings.pdf"},
    {"title": "Debate Prep Notes", "file": "econ1260_debates.docx"},
    {"title": "Final Exam Review Sheet", "file": "econ1260_final.pdf"},
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
- 📘 [Economic Policy Debate Resources](#)  
- 🎓 [Khan Academy: U.S. Economy Basics](https://www.khanacademy.org/)  
- 🎥 [YouTube Playlist: Contested Issues in Economics](#)  
- 📊 [Practice Problems – Policy Analysis](#)  
""")
