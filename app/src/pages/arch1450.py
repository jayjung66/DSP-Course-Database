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
st.title("ARCH 1450 – Understanding Design")
st.write("Welcome, {0} 👋".format(st.session_state.get('first_name', 'Student')))
st.write("Here you can view professor rankings, notes, and useful resources for this course.")

st.divider()

# -----------------------------------
# Course Overview
# -----------------------------------
st.subheader("📊 Course Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Average Enjoyment", "4/5", help="Based on student reviews")

with col2:
    st.metric("Average Difficulty", "2/5", help="Based on student reviews")

with col3:
    st.metric("Total Reviews", "1", help="Number of student reviews (ARCH 1450 only)")

st.divider()

# -----------------------------------
# Professor Reviews
# -----------------------------------
st.subheader("👨‍🏫 Professor Reviews")

# Professor: Cara Michell (1 review)
with st.expander("⭐ Professor: Cara Michell (1 review)", expanded=True):
    st.write("**Review - Solana Anderson (Spring 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐⭐ (4/5)")
    st.write("- **Difficulty:** 💪💪 (2/5)")
    st.info("**Comments:** Course was approachable and engaging. Balanced workload with clear expectations. Professor Michell made design concepts accessible and enjoyable.")
    st.success("**Exam Advice:** Focus on lecture notes and design projects. Understanding core principles is more important than memorization.")

st.divider()


# -----------------------------------
# Key Takeaways
# -----------------------------------
st.subheader("💡 Key Takeaways from Reviews")

col1, col2 = st.columns(2)

with col1:
    st.write("**Most Popular Professors (from available reviews):**")
    st.write("1. Cara Michell (ARCH 1450)")

with col2:
    st.write("**Common Themes:**")
    st.write("- Course is approachable and moderately challenging")
    st.write("- Professor makes design concepts clear and engaging")
    st.write("- Projects and lecture notes are key to success")

st.divider()

# -----------------------------------
# Study Notes
# -----------------------------------
st.subheader("📂 Available Study Notes")

notes_list = [
    {"title": "Design Principles Overview", "file": "design_principles.pdf"},
    {"title": "Architecture History Notes", "file": "arch_history.docx"},
    {"title": "Studio Project Guidelines", "file": "studio_projects.pdf"},
    {"title": "Midterm Study Guide", "file": "arch1450_midterm.pdf"},
    {"title": "Final Exam Review Sheet", "file": "arch1450_final_review.pdf"},
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
- 📘 [Open Educational Resources – Design Basics](#)  
- 🎓 [MIT OpenCourseWare: Architecture & Design](https://ocw.mit.edu/courses/architecture/)  
- 🎥 [YouTube Playlist: Understanding Design Concepts](#)  
- 🏛️ [ArchDaily – Design Inspiration](https://www.archdaily.com/)  
- 📊 [Design Thinking Resources – IDEO](https://www.ideou.com/pages/design-thinking)
""")
