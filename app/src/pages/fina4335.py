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
st.title("FINA 4335 – Computational Methods and Their Applications in Finance")
st.write("Welcome, {0} 👋".format(st.session_state.get('first_name', 'Student')))
st.write("Here you can view professor rankings, notes, and useful resources for this course.")
st.divider()

# -----------------------------------
# Course Overview
# -----------------------------------
st.subheader("📊 Course Overview")
col1, col2, col3 = st.columns(3)
with col1: st.metric("Average Enjoyment", "3/5", help="Based on student reviews")
with col2: st.metric("Average Difficulty", "2/5", help="Based on student reviews")
with col3: st.metric("Total Reviews", "1", help="Number of student reviews (FINA 4335 only)")
st.divider()

# -----------------------------------
# Professor Reviews
# -----------------------------------
st.subheader("👨‍🏫 Professor Reviews")
with st.expander("⭐ Professor: Ali Sharifkhani (1 review)", expanded=True):
    st.write("**Review - Shrey Patel (Spring 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐ (3/5)")
    st.write("- **Difficulty:** 💪💪 (2/5)")
    st.info("**Comments:** Super easy class if you already know Python, good for people who want to learn it. Easy professor, not a lot of work outside of class.")
st.divider()

# -----------------------------------
# Key Takeaways
# -----------------------------------
st.subheader("💡 Key Takeaways from Reviews")
col1, col2 = st.columns(2)
with col1: st.write("**Most Popular Professors:**\n1. Ali Sharifkhani (1 review)")
with col2: st.write("**Common Themes:**\n- Python knowledge makes class very easy\n- Light workload outside of class\n- Good introduction for students wanting to learn computational methods")
st.divider()

# -----------------------------------
# Study Notes
# -----------------------------------
st.subheader("📂 Available Study Notes")
notes_list = [
    {"title": "Python for Finance Basics", "file": "fina4335_python.pdf"},
    {"title": "Computational Methods Notes", "file": "fina4335_methods.docx"},
    {"title": "Final Exam Review Sheet", "file": "fina4335_final.pdf"},
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
- 📘 [Python for Finance Textbook](#)  
- 🎓 [Khan Academy: Programming & Finance](https://www.khanacademy.org/)  
- 🎥 [YouTube Playlist: Computational Finance Methods](#)  
- 📊 [Practice Problems – Python Applications in Finance](#)  
""")
