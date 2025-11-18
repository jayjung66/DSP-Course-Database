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
st.title("FINA 4526 – Core Topics in Alternative Investments")
st.write("Welcome, {0} 👋".format(st.session_state.get('first_name', 'Student')))
st.write("Here you can view professor rankings, notes, and useful resources for this course.")
st.divider()

# -----------------------------------
# Course Overview
# -----------------------------------
st.subheader("📊 Course Overview")
col1, col2, col3 = st.columns(3)
with col1: st.metric("Average Enjoyment", "2/5", help="Based on student reviews")
with col2: st.metric("Average Difficulty", "5/5", help="Based on student reviews")
with col3: st.metric("Total Reviews", "1", help="Number of student reviews (FINA 4526 only)")
st.divider()

# -----------------------------------
# Professor Reviews
# -----------------------------------
st.subheader("👨‍🏫 Professor Reviews")
with st.expander("⭐ Professor: Mengchao Ai (1 review)", expanded=True):
    st.write("**Review - Jessica Levesque (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐ (2/5)")
    st.write("- **Difficulty:** 💪💪💪💪💪 (5/5)")
    st.info("**Comments:** No additional comments provided.")
st.divider()

# -----------------------------------
# Key Takeaways
# -----------------------------------
st.subheader("💡 Key Takeaways from Reviews")
col1, col2 = st.columns(2)
with col1: 
    st.write("**Most Popular Professors:**")
    st.write("1. Mengchao Ai (1 review)")
with col2: 
    st.write("**Common Themes:**")
    st.write("- Very high difficulty")
    st.write("- Lower enjoyment")
    st.write("- Focused on advanced alternative investment topics")
st.divider()

# -----------------------------------
# Study Notes
# -----------------------------------
st.subheader("📂 Available Study Notes")
notes_list = [
    {"title": "Alternative Investments Case Studies", "file": "fina4526_cases.pdf"},
    {"title": "Core Topics Notes", "file": "fina4526_notes.docx"},
    {"title": "Final Exam Review Sheet", "file": "fina4526_final.pdf"},
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
- 📘 [Alternative Investments Textbook](#)  
- 🎓 [Khan Academy: Advanced Finance Topics](https://www.khanacademy.org/)  
- 🎥 [YouTube Playlist: Alternative Investments Explained](#)  
- 📊 [Practice Problems – Hedge Funds, Private Equity, Real Assets](#)  
""")
