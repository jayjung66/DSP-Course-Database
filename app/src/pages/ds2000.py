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
st.title("DS 2000 – Data Science / Programming with Data")
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
with col3: st.metric("Total Reviews", "4", help="Number of student reviews (DS 2000 only)")
st.divider()

# -----------------------------------
# Professor Reviews
# -----------------------------------
st.subheader("👨‍🏫 Professor Reviews")

# Professor: Felix Muzny
with st.expander("⭐ Professor: Felix Muzny (2 reviews)", expanded=True):
    st.write("**Review - Aidan Lothian (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐ (3/5)")
    st.write("- **Difficulty:** 💪💪 (2/5)")
    st.info("**Comments:** No exams in this course, only two mini quizzes. I would recommend taking the afternoon class and finding a friend in the morning classes... INsanely boring lecturer tbh. Your entire grade is based on weekly homeworks, just make sure that these are solid and this class is the easiest A ever.")

    st.write("**Review - Anjalika Shah (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐ (1/5)")
    st.write("- **Difficulty:** 💪 (1/5)")
    st.info("**Comments:** No additional comments provided.")

# Professor: Laney Strange
with st.expander("⭐ Professor: Laney Strange (2 reviews)", expanded=False):
    st.write("**Review - Vikram Subramanyam (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐⭐ (4/5)")
    st.write("- **Difficulty:** 💪 (1/5)")
    st.info("**Comments:** No additional comments provided.")

    st.write("**Review - Sarah Bouvier (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐⭐⭐ (5/5)")
    st.write("- **Difficulty:** 💪💪 (2/5)")
    st.info("**Comments:** She was a great teacher, very good at explaining concepts in a way that you will remember them. Definitely would recommend you take her.")
st.divider()

# -----------------------------------
# Key Takeaways
# -----------------------------------
st.subheader("💡 Key Takeaways from Reviews")
col1, col2 = st.columns(2)
with col1:
    st.write("**Most Popular Professors:**")
    st.write("1. Laney Strange (2 reviews)")
    st.write("2. Felix Muzny (2 reviews)")
with col2:
    st.write("**Common Themes:**")
    st.write("- Homework-heavy grading structure")
    st.write("- Exams minimal or non-existent")
    st.write("- Teaching style varies significantly by professor")
    st.write("- Easy to succeed with consistent effort")
st.divider()

# -----------------------------------
# Study Notes
# -----------------------------------
st.subheader("📂 Available Study Notes")
notes_list = [
    {"title": "Data Science Homework Guide", "file": "ds2000_homework.pdf"},
    {"title": "Programming with Data Concepts", "file": "ds2000_programming.docx"},
    {"title": "Final Exam Review Sheet", "file": "ds2000_final.pdf"},
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
- 📘 [Python for Data Science Basics](#)  
- 🎓 [Khan Academy: Data Science Foundations](https://www.khanacademy.org/)  
- 🎥 [YouTube Playlist: Programming with Data](#)  
- 📊 [Practice Problems – Data Structures & Analysis](#)  
""")
