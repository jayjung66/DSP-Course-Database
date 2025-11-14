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
st.title("ACCT 2301 – Profit Analysis for Managers and Advisors")
st.write("Welcome, {0} 👋".format(st.session_state.get('first_name', 'Student')))
st.write("Here you can view professor rankings, notes, and useful resources for this course.")

st.divider()

# -----------------------------------
# Course Overview
# -----------------------------------
st.subheader("📊 Course Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Average Enjoyment", "4.3/5", help="Based on student reviews")

with col2:
    st.metric("Average Difficulty", "2.6/5", help="Based on student reviews")

with col3:
    st.metric("Total Reviews", "5", help="Number of student reviews (ACCT 2301 only)")

st.divider()

# -----------------------------------
# Professor Reviews
# -----------------------------------
st.subheader("👨‍🏫 Professor Reviews")

# Professor: Udi Hoitash (2 reviews)
with st.expander("⭐ Professor: Udi Hoitash (2 reviews)", expanded=True):
    st.write("**Review #1 - Aidan Lothian (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐⭐ (4/5)")
    st.write("- **Difficulty:** 💪 (1/5)")
    st.info("**Comments:** Great teacher, super easy to connect with if you make any extra effort to talk with as you walk of class.")
    st.success("**Exam Advice:** Exam questions are literally just like the in class activities he does daily. If you go to class consistently and do the activities as he does + review slides, you will ace this class.")
    
    st.write("")
    st.write("**Review #2 - Caroline Belanger (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐⭐ (4/5)")
    st.write("- **Difficulty:** 💪💪💪 (3/5)")

# Professor: Christopher Miller (2 reviews)
with st.expander("⭐ Professor: Christopher Miller (2 reviews)", expanded=False):
    st.write("**Review #1 - Leo Harmon (Summer 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐⭐ (4/5)")
    st.write("- **Difficulty:** 💪💪💪 (3/5)")
    st.info("**Comments:** He is incredible. so funny and always available for help. taught me excel basically as all the hw is on it. two main exams. would recommend")
    
    st.write("")
    st.write("**Review #2 - Amy Park (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐⭐ (4/5)")
    st.write("- **Difficulty:** 💪💪 (2/5)")

# Professor: Mario Maletta
with st.expander("⭐ Professor: Mario Maletta (1 review)", expanded=False):
    st.write("**Review - Vikram Subramanyam (Summer 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐⭐⭐ (5/5)")
    st.write("- **Difficulty:** 💪💪 (2/5)")

st.divider()

# -----------------------------------
# Related Courses
# -----------------------------------
st.subheader("📚 Related Course Reviews")

st.info("**Note:** The following reviews are for related accounting courses (ACCT 1201 and ACCT 3401) and are included for reference.")

# ACCT 1201 - Jeremy Jones
with st.expander("📘 ACCT 1201 - Intro to Financial Accounting", expanded=False):
    st.write("**Professor: Jeremy Jones**")
    st.write("**Review - Vikram Subramanyam (Fall 2023)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐⭐⭐ (5/5)")
    st.write("- **Difficulty:** 💪💪💪 (3/5)")

# ACCT 1201 - Anthony Russo
with st.expander("📘 ACCT 1201 - Financial Accounting and Reporting", expanded=False):
    st.write("**Professor: Anthony Russo**")
    st.write("**Review - Chloe Tu (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐⭐ (4/5)")
    st.write("- **Difficulty:** 💪💪💪 (3/5)")
    st.info("**Comments:** You typically read the textbook chapter and then go over it in class and do problems which was helpful, but don't expect to be taught the material during class. He's a super funny professor though so I always enjoyed going in class. Attendance isn't technically mandatory he'll give you full points most likely if you show up enough times, super easy grader on the group project, and you can go to him to give you points back on your exams. Even if you do poorly on the exams everything else he grades are basically guaranteed 100's so you can still get an A pretty easily.")
    st.success("**Exam Advice:** Yes - materials added to study folder")

# ACCT 3401 - Yue Zhang
with st.expander("📘 ACCT 3401 - Financial Reporting and Analysis", expanded=False):
    st.write("**Professor: Yue Zhang**")
    st.write("**Review - Solana Anderson (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐⭐ (4/5)")
    st.write("- **Difficulty:** 💪💪💪💪 (4/5)")

st.divider()

# -----------------------------------
# Key Takeaways
# -----------------------------------
st.subheader("💡 Key Takeaways from Reviews")

col1, col2 = st.columns(2)

with col1:
    st.write("**Most Popular Professors:**")
    st.write("1. Udi Hoitash (2 reviews)")
    st.write("2. Christopher Miller (2 reviews)")
    st.write("3. Mario Maletta (1 review)")

with col2:
    st.write("**Common Themes:**")
    st.write("- Professors are approachable and helpful")
    st.write("- Excel skills heavily emphasized")
    st.write("- In-class activities mirror exam questions")
    st.write("- Attendance helpful but flexible")

st.divider()

# -----------------------------------
# Study Notes
# -----------------------------------
st.subheader("📂 Available Study Notes")

notes_list = [
    {"title": "Cost-Volume-Profit Analysis Guide", "file": "cvp_analysis.pdf"},
    {"title": "Budgeting & Forecasting Notes", "file": "budgeting_notes.docx"},
    {"title": "Excel Functions Cheat Sheet", "file": "excel_cheatsheet.pdf"},
    {"title": "Variance Analysis Summary", "file": "variance_analysis.pdf"},
    {"title": "Midterm Study Guide", "file": "midterm_study_guide.pdf"},
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
- 📊 [Excel for Accountants Tutorial](https://www.youtube.com/watch?v=rwbho0CgEAE)  
- 🎥 [Managerial Accounting Playlist](#)  
- 📘 [AccountingCoach - Managerial Accounting](https://www.accountingcoach.com/managerial-accounting/explanation)  
- 💼 [Corporate Finance Institute Resources](https://corporatefinanceinstitute.com/)
- 📈 [Excel Practice Problems](https://www.excel-practice-online.com/)
""")