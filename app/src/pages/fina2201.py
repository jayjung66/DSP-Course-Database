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
st.title("FINA 2201 – Financial Management")
st.write("Welcome, {0} 👋".format(st.session_state.get('first_name', 'Student')))
st.write("Here you can view professor rankings, notes, and useful resources for this course.")
st.divider()

# -----------------------------------
# Course Overview
# -----------------------------------
st.subheader("📊 Course Overview")
col1, col2, col3 = st.columns(3)
with col1: st.metric("Average Enjoyment", "3.6/5", help="Based on student reviews")
with col2: st.metric("Average Difficulty", "3.1/5", help="Based on student reviews")
with col3: st.metric("Total Reviews", "7", help="Number of student reviews (FINA 2201 only)")
st.divider()

# -----------------------------------
# Professor Reviews
# -----------------------------------
st.subheader("👨‍🏫 Professor Reviews")

# Professor: Saptarshi Mukherjee
with st.expander("⭐ Professor: Saptarshi Mukherjee (3 reviews)", expanded=True):
    st.write("**Review - Aidan Lothian (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐⭐ (4/5)")
    st.write("- **Difficulty:** 💪💪💪💪 (4/5)")
    st.info("**Comments:** Mukherjee is literally the nicest guy ever. Policy: complete all assignments = automatic B. Easy points, but exams are tough if taken honestly. Curve typically applied. Participation counts 10% even in lecture. Recommend asking questions after class so he knows your name.")

    st.write("**Review - Abigail DeMaioribus (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐⭐ (4/5)")
    st.write("- **Difficulty:** 💪💪💪 (3/5)")
    st.info("**Comments:** No additional comments provided.")

    st.write("**Review - Sarah Bouvier (Fall 2023)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐ (3/5)")
    st.write("- **Difficulty:** 💪💪 (2/5)")
    st.info("**Comments:** Very sweet professor. Homeworks and most exams online (except final). Inconsistent teaching vs homework solutions. Hard to get an A since answers are online. Exams often taken in groups; solutions appear after submission.")

# Professor: Jack Mazur
with st.expander("⭐ Professor: Jack Mazur (1 review)", expanded=False):
    st.write("**Review - Leo Harmon (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐⭐ (4/5)")
    st.write("- **Difficulty:** 💪💪 (2/5)")
    st.info("**Comments:** LOVE HIM. Looks like he was born in Fenway Park. Thick Boston accent, very kind. Rambles without slides, but explains clearly. Requires participation and strict attendance. Easy overall, highly recommended.")

# Professor: Sunayan Acharya
with st.expander("⭐ Professor: Sunayan Acharya (1 review)", expanded=False):
    st.write("**Review - Sylvia Dunaevschi (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐ (2/5)")
    st.write("- **Difficulty:** 💪💪💪💪 (4/5)")
    st.info("**Comments:** Good at teaching and helpful in office hours. Exams are difficult and no curve.")

# Professor: Mark Gooley
with st.expander("⭐ Professor: Mark Gooley (1 review)", expanded=False):
    st.write("**Review - Vikram Subramanyam (Summer 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐⭐⭐ (5/5)")
    st.write("- **Difficulty:** 💪💪💪 (3/5)")
    st.info("**Comments:** No additional comments provided.")

# Professor: Tian Tian Gu
with st.expander("⭐ Professor: Tian Tian Gu (1 review)", expanded=False):
    st.write("**Review - Chloe Tu (Spring 2025)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐ (3/5)")
    st.write("- **Difficulty:** 💪💪💪💪 (4/5)")
    st.info("**Comments:** Super sweet but lectures move very fast. Exams resemble harder practice problems. Exams online at home, final proctored in person. Attendance mandatory via code. Very understanding with scheduling flexibility.")
st.divider()

# -----------------------------------
# Key Takeaways
# -----------------------------------
st.subheader("💡 Key Takeaways from Reviews")
col1, col2 = st.columns(2)
with col1:
    st.write("**Most Popular Professors:**")
    st.write("1. Saptarshi Mukherjee (3 reviews)")
    st.write("2. Jack Mazur (1 review)")
    st.write("3. Sunayan Acharya (1 review)")
    st.write("4. Mark Gooley (1 review)")
    st.write("5. Tian Tian Gu (1 review)")
with col2:
    st.write("**Common Themes:**")
    st.write("- Exams often online, sometimes group-based")
    st.write("- Difficulty varies widely by professor")
    st.write("- Participation and attendance often required")
    st.write("- Professors generally approachable and supportive")
    st.write("- Workload manageable but exams can be tough")
st.divider()

# -----------------------------------
# Study Notes
# -----------------------------------
st.subheader("📂 Available Study Notes")
notes_list = [
    {"title": "Financial Management Midterm Study Guide", "file": "fina2201_midterm.pdf"},
    {"title": "Corporate Finance Concepts Notes", "file": "fina2201_concepts.docx"},
    {"title": "Final Exam Review Sheet", "file": "fina2201_final.pdf"},
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
- 📘 [Corporate Finance Textbook](#)  
- 🎓 [Khan Academy: Finance & Capital Markets](https://www.khanacademy.org/)  
- 🎥 [YouTube Playlist: Financial Management Concepts](#)  
- 📊 [Practice Problems – Time Value of Money & Capital Budgeting](#)  
""")
