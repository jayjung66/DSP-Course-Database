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
st.title("MKTG 3720 – Brand Management")
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
with col3: st.metric("Total Reviews", "2", help="Number of student reviews (MKTG 3720 only)")
st.divider()

# -----------------------------------
# Professor Reviews
# -----------------------------------
st.subheader("👨‍🏫 Professor Reviews")

with st.expander("⭐ Professor: Bob McCullough (1 review)", expanded=True):
    st.write("**Review - Ty Orlando (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐ (3/5)")
    st.write("- **Difficulty:** 💪💪💪 (3/5)")
    st.info("**Comments:** No additional comments provided.")

with st.expander("⭐ Professor: Chad O’Connor (1 review)", expanded=False):
    st.write("**Review - Audrey McGuff (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐⭐⭐ (5/5)")
    st.write("- **Difficulty:** 💪 (1/5)")
    st.info("**Comments:** Very funny professor.")
st.divider()

# -----------------------------------
# Key Takeaways
# -----------------------------------
st.subheader("💡 Key Takeaways from Reviews")
col1, col2 = st.columns(2)
with col1:
    st.write("**Most Popular Professors:**")
    st.write("1. Bob McCullough (1 review)")
    st.write("2. Chad O’Connor (1 review)")
with col2:
    st.write("**Common Themes:**")
    st.write("- Enjoyment varies by professor")
    st.write("- McCullough’s class moderate difficulty, average enjoyment")
    st.write("- O’Connor’s class very enjoyable and easy")
    st.write("- Humor and engagement can make the course lighter")
st.divider()

# -----------------------------------
# Study Notes
# -----------------------------------
st.subheader("📂 Available Study Notes")
notes_list = [
    {"title": "Brand Management Case Studies", "file": "mktg3720_cases.pdf"},
    {"title": "Marketing Strategy & Branding Notes", "file": "mktg3720_notes.docx"},
    {"title": "Final Exam Review Sheet", "file": "mktg3720_final.pdf"},
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
- 📘 [Brand Management Textbook](#)  
- 🎓 [Khan Academy: Marketing & Branding Basics](https://www.khanacademy.org/)  
- 🎥 [YouTube Playlist: Brand Management](#)  
- 📊 [Practice Problems – Case Analysis & Brand Strategy](#)  
""")
