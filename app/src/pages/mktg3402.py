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
st.title("MKTG 3402 – Gaining Insights from Consumer Data")
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
with col3: st.metric("Total Reviews", "2", help="Number of student reviews (MKTG 3402 only)")
st.divider()

# -----------------------------------
# Professor Reviews
# -----------------------------------
st.subheader("👨‍🏫 Professor Reviews")

with st.expander("⭐ Professor: Daniel Katz (2 reviews)", expanded=True):
    st.write("**Review - Emily Cai (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐⭐⭐ (5/5)")
    st.write("- **Difficulty:** 💪💪💪 (3/5)")
    st.info("**Comments:** Loved this class, professor is very accommodating.")

    st.write("**Review - Chloe Vergel de Dios (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐⭐⭐ (5/5)")
    st.write("- **Difficulty:** 💪💪💪 (3/5)")
    st.info("**Comments:** No additional comments provided.")
st.divider()

# -----------------------------------
# Key Takeaways
# -----------------------------------
st.subheader("💡 Key Takeaways from Reviews")
col1, col2 = st.columns(2)
with col1:
    st.write("**Most Popular Professors:**")
    st.write("1. Daniel Katz (2 reviews)")
with col2:
    st.write("**Common Themes:**")
    st.write("- Very high enjoyment")
    st.write("- Moderate difficulty")
    st.write("- Professor Katz is accommodating and supportive")
    st.write("- Strong focus on consumer data insights")
st.divider()

# -----------------------------------
# Study Notes
# -----------------------------------
st.subheader("📂 Available Study Notes")
notes_list = [
    {"title": "Consumer Data Analysis Notes", "file": "mktg3402_notes.pdf"},
    {"title": "Case Studies in Consumer Insights", "file": "mktg3402_cases.docx"},
    {"title": "Final Exam Review Sheet", "file": "mktg3402_final.pdf"},
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
- 📘 [Consumer Data & Marketing Analytics Textbook](#)  
- 🎓 [Khan Academy: Data & Marketing Basics](https://www.khanacademy.org/)  
- 🎥 [YouTube Playlist: Consumer Insights & Analytics](#)  
- 📊 [Practice Problems – Consumer Data Interpretation](#)  
""")
