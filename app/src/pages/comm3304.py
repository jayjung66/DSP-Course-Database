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
st.title("COMM 3304 – Communication and Inclusion")
st.write("Welcome, {0} 👋".format(st.session_state.get('first_name', 'Student')))
st.write("Here you can view professor rankings, notes, and useful resources for this course.")
st.divider()

# -----------------------------------
# Course Overview
# -----------------------------------
st.subheader("📊 Course Overview")
col1, col2, col3 = st.columns(3)
with col1: st.metric("Average Enjoyment", "5/5", help="Based on student reviews")
with col2: st.metric("Average Difficulty", "1/5", help="Based on student reviews")
with col3: st.metric("Total Reviews", "1", help="Number of student reviews (COMM 3304 only)")
st.divider()

# -----------------------------------
# Professor Reviews
# -----------------------------------
st.subheader("👨‍🏫 Professor Reviews")
with st.expander("⭐ Professor: Patricia Davis (1 review)", expanded=True):
    st.write("**Review - Audrey McGuff (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐⭐⭐ (5/5)")
    st.write("- **Difficulty:** 💪 (1/5)")
    st.info("**Comments:** Super understanding professor")
st.divider()

# -----------------------------------
# Key Takeaways
# -----------------------------------
st.subheader("💡 Key Takeaways from Reviews")
col1, col2 = st.columns(2)
with col1: st.write("**Most Popular Professors:**\n1. Patricia Davis (1 review)")
with col2: st.write("**Common Themes:**\n- Very approachable professor\n- Easy workload\n- High enjoyment")
st.divider()

# -----------------------------------
# Study Notes
# -----------------------------------
st.subheader("📂 Available Study Notes")
notes_list = [{"title": "Communication & Inclusion Guide", "file": "comm3304_notes.pdf"}]
for note in notes_list:
    st.download_button(label=f"📄 {note['title']}", file_name=note['file'], data=f"Dummy content for {note['file']}")
st.divider()

# -----------------------------------
# Other Resources
# -----------------------------------
st.subheader("📖 Additional Resources")
st.markdown("""
- 📘 [Inclusive Communication Practices](#)  
- 🎓 [Diversity & Inclusion in Communication](#)  
""")
