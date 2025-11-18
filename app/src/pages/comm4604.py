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
st.title("COMM 4604 – Youth and Communication Technology")
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
with col3: st.metric("Total Reviews", "1", help="Number of student reviews (COMM 4604 only)")
st.divider()

# -----------------------------------
# Professor Reviews
# -----------------------------------
st.subheader("👨‍🏫 Professor Reviews")

with st.expander("⭐ Professor: Meryl Alper (1 review)", expanded=True):
    st.write("**Review - Katie Kerl (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐⭐ (4/5)")
    st.write("- **Difficulty:** 💪 (1/5)")
    st.info("**Comments:** Best/easiest Comm writing intensive for sure!!")
st.divider()

# -----------------------------------
# Key Takeaways
# -----------------------------------
st.subheader("💡 Key Takeaways from Reviews")
col1, col2 = st.columns(2)
with col1:
    st.write("**Most Popular Professors:**")
    st.write("1. Meryl Alper (1 review)")
with col2:
    st.write("**Common Themes:**")
    st.write("- Very easy workload (1/5 difficulty)")
    st.write("- Positive enjoyment (4/5)")
    st.write("- Considered the easiest Comm writing intensive option")
st.divider()

# -----------------------------------
# Study Notes
# -----------------------------------
st.subheader("📂 Available Study Notes")
notes_list = [
    {"title": "Youth & Communication Technology Notes", "file": "comm4604_notes.pdf"},
    {"title": "Case Studies in Communication Tech", "file": "comm4604_cases.docx"},
    {"title": "Final Exam Review Sheet", "file": "comm4604_final.pdf"},
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
- 📘 [Youth & Communication Technology Textbook](#)  
- 🎓 [Khan Academy: Communication Basics](https://www.khanacademy.org/)  
- 🎥 [YouTube Playlist: Communication Technology](#)  
- 📊 [Practice Problems – Media & Youth Case Analysis](#)  
""")
