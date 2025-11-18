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
st.title("FINA 4219 – Portfolio Management")
st.write("Welcome, {0} 👋".format(st.session_state.get('first_name', 'Student')))
st.write("Here you can view professor rankings, notes, and useful resources for this course.")
st.divider()

# -----------------------------------
# Course Overview
# -----------------------------------
st.subheader("📊 Course Overview")
col1, col2, col3 = st.columns(3)
with col1: st.metric("Average Enjoyment", "5/5", help="Based on student reviews")
with col2: st.metric("Average Difficulty", "3/5", help="Based on student reviews")
with col3: st.metric("Total Reviews", "1", help="Number of student reviews (FINA 4219 only)")
st.divider()

# -----------------------------------
# Professor Reviews
# -----------------------------------
st.subheader("👨‍🏫 Professor Reviews")
with st.expander("⭐ Professor: Joseph Marks (1 review)", expanded=True):
    st.write("**Review - Shrey Patel (Spring 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐⭐⭐ (5/5)")
    st.write("- **Difficulty:** 💪💪💪 (3/5)")
    st.info("**Comments:** Amazing professor, class is very straightforward and not hard to do well in if you put in the effort. Two projects and 4 exams, but no other take-home work.")
st.divider()

# -----------------------------------
# Key Takeaways
# -----------------------------------
st.subheader("💡 Key Takeaways from Reviews")
col1, col2 = st.columns(2)
with col1: st.write("**Most Popular Professors:**\n1. Joseph Marks (1 review)")
with col2: st.write("**Common Themes:**\n- Straightforward structure\n- Two projects and four exams\n- No take-home assignments\n- Effort leads to success")
st.divider()

# -----------------------------------
# Study Notes
# -----------------------------------
st.subheader("📂 Available Study Notes")
notes_list = [
    {"title": "Portfolio Management Project Guide", "file": "fina4219_projects.pdf"},
    {"title": "Exam Preparation Notes", "file": "fina4219_exams.docx"},
    {"title": "Final Exam Review Sheet", "file": "fina4219_final.pdf"},
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
- 📘 [Portfolio Management Textbook](#)  
- 🎓 [Khan Academy: Investing & Portfolio Basics](https://www.khanacademy.org/)  
- 🎥 [YouTube Playlist: Portfolio Management Explained](#)  
- 📊 [Practice Problems – Risk & Diversification](#)  
""")
