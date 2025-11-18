import logging
logger = logging.getLogger(__name__)
import requests

import streamlit as st
from modules.nav import SideBarLinks

# Set the API base URL
API_BASE = "http://web-api:4000"

st.set_page_config(layout='wide')

# Sidebar
SideBarLinks()

# Back button
if st.button("⬅️ Back to Home"):
    st.switch_page('Home.py')

# -----------------------------------
# Page Content
# -----------------------------------
st.title("CS 2500 – Fundamentals of Computer Science 1")
st.write("Welcome, {0} 👋".format(st.session_state.get('first_name', 'Student')))
st.write("Here you can view professor rankings, notes, and useful resources for this course.")

st.divider()

# -----------------------------------
# Course Overview
# -----------------------------------
st.subheader("📊 Course Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Average Enjoyment", "4/5", help="Based on student reviews")

with col2:
    st.metric("Average Difficulty", "3/5", help="Based on student reviews")

with col3:
    st.metric("Total Reviews", "1", help="Number of student reviews (CS 2500 only)")

st.divider()

# -----------------------------------
# Professor Reviews
# -----------------------------------
st.subheader("👨‍🏫 Professor Reviews")

# Professor: John Park (1 review)
with st.expander("⭐ Professor: John Park (1 review)", expanded=True):
    st.write("**Review - Chloe Tu (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐⭐ (4/5)")
    st.write("- **Difficulty:** 💪💪💪 (3/5)")
    st.info("**Comments:** I didn't think it was necessarily hard but you definitely have to spend a decent amount of time to understand it and do the hw's. Definitely utilize the TA's a lot—they were super helpful. Start the hw's early because you can have 1-on-1's with them and they can basically tutor you. Not sure if it will be the same since they are changing the fundies curriculum but John Park was such a sweet professor.")
    st.success("**Exam Advice:** His tests were all writing code, which made them predictable. If you've taken AP CSA in high school, it's similar to the free response section. Exams were fair, and curves helped—ended up with an A.")

st.divider()

# -----------------------------------
# Related Courses
# -----------------------------------
st.subheader("📚 Related Course Reviews")

st.info("**Note:** The following reviews are for related computer science courses and are included for reference.")

# Example related course
with st.expander("📘 CS 2510 – Fundamentals of Computer Science 2", expanded=False):
    st.write("**Professor: TBD**")
    st.write("**Review:** Coming soon...")

st.divider()

# -----------------------------------
# Key Takeaways
# -----------------------------------
st.subheader("💡 Key Takeaways from Reviews")

col1, col2 = st.columns(2)

with col1:
    st.write("**Most Popular Professors (from available reviews):**")
    st.write("1. John Park (CS 2500)")

with col2:
    st.write("**Common Themes:**")
    st.write("- Homework requires consistent effort and early start")
    st.write("- TA support is crucial and highly recommended")
    st.write("- Exams focus on writing code, predictable format")
    st.write("- Professor is approachable and supportive")

st.divider()

# -----------------------------------
# Study Notes
# -----------------------------------
st.subheader("📂 Available Study Notes")

notes_list = [
    {"title": "CS 2500 Midterm Study Guide", "file": "cs2500_midterm.pdf"},
    {"title": "Fundies Curriculum Notes", "file": "fundies_notes.docx"},
    {"title": "Common Coding Patterns Cheat Sheet", "file": "coding_patterns.pdf"},
    {"title": "Practice Problems – Recursion & Loops", "file": "recursion_loops.pdf"},
    {"title": "Final Exam Review Sheet", "file": "cs2500_final_review.pdf"},
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
- 💻 [Northeastern CS 2500 Course Page](#)  
- 🎓 [Khan Academy: Computer Science Basics](https://www.khanacademy.org/computing/computer-science)  
- 📘 [CS50 Harvard – Intro to Computer Science](https://cs50.harvard.edu/x/)  
- 📝 [Practice Coding Problems – LeetCode](https://leetcode.com/)  
- 📊 [CodingBat – Java & Python Practice](https://codingbat.com/)
""")
