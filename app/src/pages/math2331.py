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
st.title("MATH 2331 – Linear Algebra")
st.write("Welcome, {0} 👋".format(st.session_state.get('first_name', 'Student')))
st.write("Here you can view professor rankings, notes, and useful resources for this course.")
st.divider()

# -----------------------------------
# Course Overview
# -----------------------------------
st.subheader("📊 Course Overview")
col1, col2, col3 = st.columns(3)
with col1: st.metric("Average Enjoyment", "4/5", help="Based on student reviews")
with col2: st.metric("Average Difficulty", "3/5", help="Based on student reviews")
with col3: st.metric("Total Reviews", "1", help="Number of student reviews (MATH 2331 only)")
st.divider()

# -----------------------------------
# Professor Reviews
# -----------------------------------
st.subheader("👨‍🏫 Professor Reviews")
with st.expander("⭐ Professor: Valerie Hower (1 review)", expanded=True):
    st.write("**Review - Shrey Patel (Spring 2025)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐⭐ (4/5)")
    st.write("- **Difficulty:** 💪💪💪 (3/5)")
    st.info("**Comments:** Goated professor, take her if possible.")
st.divider()

# -----------------------------------
# Key Takeaways
# -----------------------------------
st.subheader("💡 Key Takeaways from Reviews")
col1, col2 = st.columns(2)
with col1:
    st.write("**Most Popular Professors:**")
    st.write("1. Valerie Hower (1 review)")
with col2:
    st.write("**Common Themes:**")
    st.write("- Highly recommended professor")
    st.write("- Moderate difficulty level")
    st.write("- Strong teaching reputation")
st.divider()

# -----------------------------------
# Study Notes
# -----------------------------------
st.subheader("📂 Available Study Notes")
notes_list = [
    {"title": "Linear Algebra Lecture Notes", "file": "math2331_notes.pdf"},
    {"title": "Matrix Operations & Eigenvalues", "file": "math2331_matrices.docx"},
    {"title": "Final Exam Review Sheet", "file": "math2331_final.pdf"},
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
- 📘 [Linear Algebra Textbook](#)  
- 🎓 [Khan Academy: Linear Algebra](https://www.khanacademy.org/)  
- 🎥 [YouTube Playlist: Linear Algebra Explained](#)  
- 📊 [Practice Problems – Matrices, Eigenvalues, Vector Spaces](#)  
""")
