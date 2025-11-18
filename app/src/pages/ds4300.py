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
st.title("DS 4300 – Large Scale Information Storage and Retrieval")
st.write("Welcome, {0} 👋".format(st.session_state.get('first_name', 'Student')))
st.write("Here you can view professor rankings, notes, and useful resources for this course.")
st.divider()

# -----------------------------------
# Course Overview
# -----------------------------------
st.subheader("📊 Course Overview")
col1, col2, col3 = st.columns(3)
with col1: st.metric("Average Enjoyment", "3/5", help="Based on student reviews")
with col2: st.metric("Average Difficulty", "3/5", help="Based on student reviews")
with col3: st.metric("Total Reviews", "1", help="Number of student reviews (DS 4300 only)")
st.divider()

# -----------------------------------
# Professor Reviews
# -----------------------------------
st.subheader("👨‍🏫 Professor Reviews")
with st.expander("⭐ Professor: Mark Fontenot (1 review)", expanded=True):
    st.write("**Review - Shrey Patel (Spring 2025)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐ (3/5)")
    st.write("- **Difficulty:** 💪💪💪 (3/5)")
    st.info("**Comments:** Class is more useful for people who want to go into SWE or data engineering. I dislike Fontenot's overall teaching style but he expects us to do a good amount of our own research which is good for simulating real world stuff. Not a lot of work which is nice.")
st.divider()

# -----------------------------------
# Key Takeaways
# -----------------------------------
st.subheader("💡 Key Takeaways from Reviews")
col1, col2 = st.columns(2)
with col1: st.write("**Most Popular Professors:**\n1. Mark Fontenot (1 review)")
with col2: st.write("**Common Themes:**\n- Moderate difficulty\n- Useful for SWE/data engineering paths\n- Teaching style requires independent research\n- Workload is relatively light")
st.divider()

# -----------------------------------
# Study Notes
# -----------------------------------
st.subheader("📂 Available Study Notes")
notes_list = [
    {"title": "Information Storage Concepts", "file": "ds4300_storage.pdf"},
    {"title": "Retrieval Systems Notes", "file": "ds4300_retrieval.docx"},
    {"title": "Final Exam Review Sheet", "file": "ds4300_final.pdf"},
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
- 📘 [Database Systems Concepts](#)  
- 🎓 [Khan Academy: Data Engineering Basics](https://www.khanacademy.org/)  
- 🎥 [YouTube Playlist: Large Scale Storage & Retrieval](#)  
- 📊 [Practice Problems – Information Retrieval](#)  
""")
