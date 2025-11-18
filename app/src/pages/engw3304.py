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
st.title("ENGW 3304 – Advanced Writing in the Disciplines for Business Professionals")
st.write("Welcome, {0} 👋".format(st.session_state.get('first_name', 'Student')))
st.write("Here you can view professor rankings, notes, and useful resources for this course.")
st.divider()

# -----------------------------------
# Course Overview
# -----------------------------------
st.subheader("📊 Course Overview")
col1, col2, col3 = st.columns(3)
with col1: st.metric("Average Enjoyment", "3.7/5", help="Based on student reviews")
with col2: st.metric("Average Difficulty", "1.3/5", help="Based on student reviews")
with col3: st.metric("Total Reviews", "3", help="Number of student reviews (ENGW 3304 only)")
st.divider()

# -----------------------------------
# Professor Reviews
# -----------------------------------
st.subheader("👨‍🏫 Professor Reviews")

# Professor: Elly Jackson
with st.expander("⭐ Professor: Elly Jackson (1 review)", expanded=True):
    st.write("**Review - Sarah Bouvier (Fall 2024)**")
    st.write("- **Format:** In Person (also teaches online)")
    st.write("- **Enjoyment:** ⭐⭐⭐ (3/5)")
    st.write("- **Difficulty:** 💪 (1/5)")
    st.info("**Comments:** TAKE HER. It was so easy and she is so incredibly sweet. I took it online, she also teaches in person. If you can choose between the two, take online, I've heard the actual going to class is a waste of time. Regardless, she is amazing. She grades very nicely, workload is very small. I wrote one actual paper the entire semester and it was an 8 page research paper. Otherwise, small projects and easy write ups. Take her 100%.")

# Professor: David Ober
with st.expander("⭐ Professor: David Ober (1 review)", expanded=False):
    st.write("**Review - Joao Andrade Merjam (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐ (3/5)")
    st.write("- **Difficulty:** 💪💪 (2/5)")
    st.info("**Comments:** Class was a little disorganized, and very boring. Work is very doable, just can be a lot of writing at times, probably much easier to do online.")

# Professor: Jonathan Benda
with st.expander("⭐ Professor: Jonathan Benda (1 review)", expanded=False):
    st.write("**Review - Susan Huang (Spring 2025)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐⭐⭐ (5/5)")
    st.write("- **Difficulty:** 💪 (1/5)")
    st.info("**Comments:** He is super nice and honestly grades pretty easily. Only three big essays throughout the semester, and he gives you a lot of class time to work on them.")
st.divider()

# -----------------------------------
# Key Takeaways
# -----------------------------------
st.subheader("💡 Key Takeaways from Reviews")
col1, col2 = st.columns(2)
with col1:
    st.write("**Most Popular Professors:**")
    st.write("1. Elly Jackson (1 review)")
    st.write("2. David Ober (1 review)")
    st.write("3. Jonathan Benda (1 review)")
with col2:
    st.write("**Common Themes:**")
    st.write("- Workload varies by professor")
    st.write("- Online format often easier")
    st.write("- Generally light grading and manageable assignments")
    st.write("- Writing-intensive but not overwhelming")
st.divider()

# -----------------------------------
# Study Notes
# -----------------------------------
st.subheader("📂 Available Study Notes")
notes_list = [
    {"title": "Business Writing Research Paper Guide", "file": "engw3304_research.pdf"},
    {"title": "Essay Planning Notes", "file": "engw3304_essays.docx"},
    {"title": "Final Exam Review Sheet", "file": "engw3304_final.pdf"},
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
- 📘 [Business Writing Essentials](#)  
- 🎓 [Khan Academy: Writing & Communication](https://www.khanacademy.org/)  
- 🎥 [YouTube Playlist: Advanced Writing for Business](#)  
- 📊 [Practice Problems – Writing in Business Contexts](#)  
""")
