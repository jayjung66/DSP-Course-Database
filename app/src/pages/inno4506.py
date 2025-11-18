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
st.title("INNO 4506 – Integrated Studies in Social Innovation and Entrepreneurship")
st.write("Welcome, {0} 👋".format(st.session_state.get('first_name', 'Student')))
st.write("Here you can view professor rankings, notes, and useful resources for this course.")
st.divider()

# -----------------------------------
# Course Overview
# -----------------------------------
st.subheader("📊 Course Overview")
col1, col2, col3 = st.columns(3)
with col1: st.metric("Average Enjoyment", "4/5", help="Based on student reviews")
with col2: st.metric("Average Difficulty", "2/5", help="Based on student reviews")
with col3: st.metric("Total Reviews", "2", help="Number of student reviews (INNO 4506 only)")
st.divider()

# -----------------------------------
# Professor Reviews
# -----------------------------------
st.subheader("👨‍🏫 Professor Reviews")
with st.expander("⭐ Professor: Nikki James (2 reviews)", expanded=True):
    st.write("**Review - Joao Andrade Merjam (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐⭐ (4/5)")
    st.write("- **Difficulty:** 💪💪 (2/5)")
    st.info("**Comments:** I really enjoyed this class, which is a capstone for Social Innovation and Entrepreneurship concentration. Dr. Nikki is very knowledgeable and makes the class very interactive. Class is just a big final team project that you present to professionals that Dr. Nikki brings in.")

    st.write("**Review - Natalie Acker (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐⭐ (4/5)")
    st.write("- **Difficulty:** 💪💪 (2/5)")
    st.info("**Comments:** No additional comments provided.")
st.divider()

# -----------------------------------
# Key Takeaways
# -----------------------------------
st.subheader("💡 Key Takeaways from Reviews")
col1, col2 = st.columns(2)
with col1:
    st.write("**Most Popular Professors:**")
    st.write("1. Nikki James (2 reviews)")
with col2:
    st.write("**Common Themes:**")
    st.write("- Capstone course for Social Innovation & Entrepreneurship")
    st.write("- Highly interactive teaching style")
    st.write("- Final team project presented to professionals")
    st.write("- Moderate difficulty, strong enjoyment")
st.divider()

# -----------------------------------
# Study Notes
# -----------------------------------
st.subheader("📂 Available Study Notes")
notes_list = [
    {"title": "Capstone Project Guide", "file": "inno4506_project.pdf"},
    {"title": "Social Innovation Case Studies", "file": "inno4506_cases.docx"},
    {"title": "Final Presentation Prep Sheet", "file": "inno4506_final.pdf"},
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
- 📘 [Social Innovation & Entrepreneurship Textbook](#)  
- 🎓 [Khan Academy: Business & Social Impact](https://www.khanacademy.org/)  
- 🎥 [YouTube Playlist: Social Innovation & Entrepreneurship](#)  
- 📊 [Practice Problems – Capstone Project Planning](#)  
""")
