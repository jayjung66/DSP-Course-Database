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
st.title("BIOL 1147 – The Human Organism")
st.write("Welcome, {0} 👋".format(st.session_state.get('first_name', 'Student')))
st.write("Here you can view professor rankings, notes, and useful resources for this course.")

st.divider()

# -----------------------------------
# Course Overview
# -----------------------------------
st.subheader("📊 Course Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Average Enjoyment", "3/5", help="Based on student reviews")

with col2:
    st.metric("Average Difficulty", "1/5", help="Based on student reviews")

with col3:
    st.metric("Total Reviews", "1", help="Number of student reviews (BIOL 1147 only)")

st.divider()

# -----------------------------------
# Professor Reviews
# -----------------------------------
st.subheader("👨‍🏫 Professor Reviews")

# Professor: Patricia Hampf (1 review)
with st.expander("⭐ Professor: Patricia Hampf (1 review)", expanded=True):
    st.write("**Review - Amy Park (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐ (3/5)")
    st.write("- **Difficulty:** 💪 (1/5)")

st.divider()

# -----------------------------------
# Key Takeaways
# -----------------------------------
st.subheader("💡 Key Takeaways from Reviews")

col1, col2 = st.columns(2)

with col1:
    st.write("**Most Popular Professors:**")
    st.write("1. Patricia Hampf (1 review)")

with col2:
    st.write("**Common Themes:**")
    st.write("- Course is approachable")
    st.write("- Low difficulty level")
    st.write("- Moderate enjoyment")

st.divider()

# -----------------------------------
# Study Notes
# -----------------------------------
st.subheader("📂 Available Study Notes")

notes_list = [
    {"title": "Human Organism Midterm Study Guide", "file": "human_midterm.pdf"},
    {"title": "Body Systems Overview", "file": "body_systems.docx"},
    {"title": "Final Exam Review Sheet", "file": "human_final_review.pdf"},
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
- 📘 [OpenStax Biology Textbook](https://openstax.org/books/biology-2e/pages/1-introduction)  
- 🎓 [Khan Academy: Human Biology](https://www.khanacademy.org/science/biology)  
""")
