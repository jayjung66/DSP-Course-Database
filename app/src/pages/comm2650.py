import logging
logger = logging.getLogger(__name__)
import requests
import streamlit as st
from modules.nav import SideBarLinks

API_BASE = "http://web-api:4000"
st.set_page_config(layout='wide')
SideBarLinks()

if st.button("⬅️ Back to Home"):
    st.switch_page('Home.py')

# -----------------------------------
# Page Content
# -----------------------------------
st.title("COMM 2650 – The Business of Entertainment")
st.write("Welcome, {0} 👋".format(st.session_state.get('first_name', 'Student')))
st.write("Here you can view professor rankings, notes, and useful resources for this course.")
st.divider()

# -----------------------------------
# Course Overview
# -----------------------------------
st.subheader("📊 Course Overview")
col1, col2, col3 = st.columns(3)
with col1: st.metric("Average Enjoyment", "3/5", help="Based on student reviews")
with col2: st.metric("Average Difficulty", "1/5", help="Based on student reviews")
with col3: st.metric("Total Reviews", "1", help="Number of student reviews (COMM 2650 only)")
st.divider()

# -----------------------------------
# Professor Reviews
# -----------------------------------
st.subheader("👨‍🏫 Professor Reviews")
with st.expander("⭐ Professor: Bill Lancaster (1 review)", expanded=True):
    st.write("**Review - Sarah Bouvier (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐ (3/5)")
    st.write("- **Difficulty:** 💪 (1/5)")
    st.info("**Comments:** This class is fine. I took it as a blow off NU Path class. Professor is nice, but everything we do feels like an actual waste of time. The assignments are pointless, the quizzes are soooo hyperspecific (it's fine because it's not lockdown browser), and you do all these presentations that don't really count for anything other than your participation grade. The class wasn't hard, just not really a good use of time.")
st.divider()

# -----------------------------------
# Key Takeaways
# -----------------------------------
st.subheader("💡 Key Takeaways from Reviews")
col1, col2 = st.columns(2)
with col1: st.write("**Most Popular Professors:**\n1. Bill Lancaster (1 review)")
with col2: st.write("**Common Themes:**\n- Easy workload\n- Low enjoyment\n- Assignments not meaningful")
st.divider()

# -----------------------------------
# Study Notes
# -----------------------------------
st.subheader("📂 Available Study Notes")
notes_list = [
    {"title": "Entertainment Industry Overview", "file": "comm2650_overview.pdf"},
    {"title": "Quiz Prep Guide", "file": "comm2650_quizprep.docx"},
]
for note in notes_list:
    st.download_button(label=f"📄 {note['title']}", file_name=note['file'], data=f"Dummy content for {note['file']}")
st.divider()

# -----------------------------------
# Other Resources
# -----------------------------------
st.subheader("📖 Additional Resources")
st.markdown("""
- 📘 [Entertainment Business Insights](#)  
- 🎓 [NU Path Requirements Guide](#)  
""")
