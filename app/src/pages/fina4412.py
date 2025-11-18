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
st.title("FINA 4412 – Personal Financial Planning")
st.write("Welcome, {0} 👋".format(st.session_state.get('first_name', 'Student')))
st.write("Here you can view professor rankings, notes, and useful resources for this course.")
st.divider()

# -----------------------------------
# Course Overview
# -----------------------------------
st.subheader("📊 Course Overview")
col1, col2, col3 = st.columns(3)
with col1: st.metric("Average Enjoyment", "2/5", help="Based on student reviews")
with col2: st.metric("Average Difficulty", "1/5", help="Based on student reviews")
with col3: st.metric("Total Reviews", "1", help="Number of student reviews (FINA 4412 only)")
st.divider()

# -----------------------------------
# Professor Reviews
# -----------------------------------
st.subheader("👨‍🏫 Professor Reviews")
with st.expander("⭐ Professor: Vincent Muscolino (1 review)", expanded=True):
    st.write("**Review - Susan Huang (Spring 2025)**")
    st.write("- **Format:** Online")
    st.write("- **Enjoyment:** ⭐⭐ (2/5)")
    st.write("- **Difficulty:** 💪 (1/5)")
    st.info("**Comments:** Overall very easy finance elective, but the professor is very unorganized. His exams are hard but homework assignments are very easy 100. Would recommend going in with a good group since there is a lot of group work.")
st.divider()

# -----------------------------------
# Key Takeaways
# -----------------------------------
st.subheader("💡 Key Takeaways from Reviews")
col1, col2 = st.columns(2)
with col1: st.write("**Most Popular Professors:**\n1. Vincent Muscolino (1 review)")
with col2: st.write("**Common Themes:**\n- Easy elective overall\n- Exams are difficult compared to homework\n- Heavy group work component\n- Professor organization could be improved")
st.divider()

# -----------------------------------
# Study Notes
# -----------------------------------
st.subheader("📂 Available Study Notes")
notes_list = [
    {"title": "Personal Financial Planning Homework Guide", "file": "fina4412_homework.pdf"},
    {"title": "Group Project Notes", "file": "fina4412_projects.docx"},
    {"title": "Final Exam Review Sheet", "file": "fina4412_final.pdf"},
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
- 📘 [Personal Finance Planning Textbook](#)  
- 🎓 [Khan Academy: Personal Finance](https://www.khanacademy.org/)  
- 🎥 [YouTube Playlist: Financial Planning Basics](#)  
- 📊 [Practice Problems – Retirement & Investment Planning](#)  
""")
