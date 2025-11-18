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
st.title("MATH 2341 – Differential Equations and Linear Algebra")
st.write("Welcome, {0} 👋".format(st.session_state.get('first_name', 'Student')))
st.write("Here you can view professor rankings, notes, and useful resources for this course.")
st.divider()

# -----------------------------------
# Course Overview
# -----------------------------------
st.subheader("📊 Course Overview")
col1, col2, col3 = st.columns(3)
with col1: st.metric("Average Enjoyment", "3/5", help="Based on student reviews")
with col2: st.metric("Average Difficulty", "5/5", help="Based on student reviews")
with col3: st.metric("Total Reviews", "1", help="Number of student reviews (MATH 2341 only)")
st.divider()

# -----------------------------------
# Professor Reviews
# -----------------------------------
st.subheader("👨‍🏫 Professor Reviews")
with st.expander("⭐ Professor: Bob Lupi (1 review)", expanded=True):
    st.write("**Review - Krystal Zepaj (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐ (3/5)")
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
    st.write("1. Bob Lupi (1 review)")
with col2:
    st.write("**Common Themes:**")
    st.write("- Very high difficulty")
    st.write("- Moderate enjoyment")
    st.write("- Heavy focus on both differential equations and linear algebra concepts")
st.divider()

# -----------------------------------
# Study Notes
# -----------------------------------
st.subheader("📂 Available Study Notes")
notes_list = [
    {"title": "Differential Equations Problem Set", "file": "math2341_diff_eqs.pdf"},
    {"title": "Linear Algebra Applications Notes", "file": "math2341_linear.docx"},
    {"title": "Final Exam Review Sheet", "file": "math2341_final.pdf"},
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
- 📘 [Differential Equations & Linear Algebra Textbook](#)  
- 🎓 [Khan Academy: Differential Equations](https://www.khanacademy.org/)  
- 🎥 [YouTube Playlist: Differential Equations & Linear Algebra](#)  
- 📊 [Practice Problems – Systems of Equations & ODEs](#)  
""")
