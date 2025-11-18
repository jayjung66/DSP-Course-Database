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
st.title("DS 2001 – Data Science Programming Practicum")
st.write("Welcome, {0} 👋".format(st.session_state.get('first_name', 'Student')))
st.write("Here you can view professor rankings, notes, and useful resources for this course.")
st.divider()

# -----------------------------------
# Course Overview
# -----------------------------------
st.subheader("📊 Course Overview")
col1, col2, col3 = st.columns(3)
with col1: st.metric("Average Enjoyment", "3/5", help="Based on student reviews")
with col2: st.metric("Average Difficulty", "1/5", help="Based on student reviews")
with col3: st.metric("Total Reviews", "1", help="Number of student reviews (DS 2001 only)")
st.divider()

# -----------------------------------
# Professor Reviews
# -----------------------------------
st.subheader("👨‍🏫 Professor Reviews")
with st.expander("⭐ Professor: Yi Yin (1 review)", expanded=True):
    st.write("**Review - Sarah Bouvier (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐ (3/5)")
    st.write("- **Difficulty:** 💪 (1/5)")
    st.info("**Comments:** She was okay, very sweet but not the best at teaching. She would make errors a fair amount and when you had issues, she usually was not much help. It's just the practicum though, so if you end up with her, I wouldn't stress it. The assignments are easy.")
st.divider()

# -----------------------------------
# Key Takeaways
# -----------------------------------
st.subheader("💡 Key Takeaways from Reviews")
col1, col2 = st.columns(2)
with col1: st.write("**Most Popular Professors:**\n1. Yi Yin (1 review)")
with col2: st.write("**Common Themes:**\n- Easy assignments\n- Practicum format less stressful\n- Teaching style described as kind but error-prone")
st.divider()

# -----------------------------------
# Study Notes
# -----------------------------------
st.subheader("📂 Available Study Notes")
notes_list = [
    {"title": "Programming Practicum Homework Guide", "file": "ds2001_homework.pdf"},
    {"title": "Common Errors & Fixes Notes", "file": "ds2001_errors.docx"},
    {"title": "Final Practicum Review Sheet", "file": "ds2001_final.pdf"},
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
- 📘 [Python Programming Basics](#)  
- 🎓 [Khan Academy: Intro to Programming](https://www.khanacademy.org/)  
- 🎥 [YouTube Playlist: Data Science Practicum Tips](#)  
- 📊 [Practice Problems – Programming Fundamentals](#)  
""")
