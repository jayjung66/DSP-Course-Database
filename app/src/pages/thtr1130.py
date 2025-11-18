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
st.title("THTR 1130 – Introduction to Acting")
st.write("Welcome, {0} 👋".format(st.session_state.get('first_name', 'Student')))
st.write("Here you can view professor rankings, notes, and useful resources for this course.")
st.divider()

# -----------------------------------
# Course Overview
# -----------------------------------
st.subheader("📊 Course Overview")
col1, col2, col3 = st.columns(3)
with col1: st.metric("Average Enjoyment", "5/5", help="Based on student reviews")
with col2: st.metric("Average Difficulty", "1/5", help="Based on student reviews")
with col3: st.metric("Total Reviews", "1", help="Number of student reviews (THTR 1130 only)")
st.divider()

# -----------------------------------
# Professor Reviews
# -----------------------------------
st.subheader("👨‍🏫 Professor Reviews")

with st.expander("⭐ Professor: Samantha Boehm (1 review)", expanded=True):
    st.write("**Review - Luke Noble (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐⭐⭐ (5/5)")
    st.write("- **Difficulty:** 💪 (1/5)")
    st.info("**Comments:** Mickey Mouse creative expression credit, ridiculously easy.")
st.divider()

# -----------------------------------
# Key Takeaways
# -----------------------------------
st.subheader("💡 Key Takeaways from Reviews")
col1, col2 = st.columns(2)
with col1:
    st.write("**Most Popular Professors:**")
    st.write("1. Samantha Boehm (1 review)")
with col2:
    st.write("**Common Themes:**")
    st.write("- Extremely easy workload")
    st.write("- Very high enjoyment")
    st.write("- Functions as a creative expression credit")
st.divider()

# -----------------------------------
# Study Notes
# -----------------------------------
st.subheader("📂 Available Study Notes")
notes_list = [
    {"title": "Acting Basics Notes", "file": "thtr1130_notes.pdf"},
    {"title": "Scene Study Exercises", "file": "thtr1130_cases.docx"},
    {"title": "Final Exam Review Sheet", "file": "thtr1130_final.pdf"},
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
- 📘 [Introduction to Acting Textbook](#)  
- 🎓 [Khan Academy: Theater & Performance Basics](https://www.khanacademy.org/)  
- 🎥 [YouTube Playlist: Acting Fundamentals](#)  
- 📊 [Practice Exercises – Monologues & Scene Work](#)  
""")
