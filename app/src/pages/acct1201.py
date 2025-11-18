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
st.title("ACCT 1201 – Intro to Financial Accounting")
st.write("Welcome, {0} 👋".format(st.session_state.get('first_name', 'Student')))
st.write("Here you can view professor rankings, notes, and useful resources for this course.")

st.divider()

# -----------------------------------
# Course Overview
# -----------------------------------
st.subheader("📊 Course Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Average Enjoyment", "4.4/5", help="Based on student reviews")

with col2:
    st.metric("Average Difficulty", "3.0/5", help="Based on student reviews")

with col3:
    st.metric("Total Reviews", "4", help="Number of student reviews (ACCT 1201 only)")

st.divider()

# -----------------------------------
# Professor Reviews
# -----------------------------------
st.subheader("👨‍🏫 Professor Reviews")

# Professor: Jeremy Jones
with st.expander("⭐ Professor: Jeremy Jones (1 review)", expanded=True):
    st.write("**Review - Vikram Subramanyam (Fall 2023)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐⭐⭐ (5/5)")
    st.write("- **Difficulty:** 💪💪💪 (3/5)")
    st.info("**Comments:** Clear explanations and approachable. Good balance between theory and practice.")
    st.success("**Exam Advice:** Focus on textbook problems and practice sets.")

# Professor: Anthony Russo
with st.expander("⭐ Professor: Anthony Russo (1 review)", expanded=False):
    st.write("**Review - Chloe Tu (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐⭐ (4/5)")
    st.write("- **Difficulty:** 💪💪💪 (3/5)")
    st.info("**Comments:** Funny professor, makes class enjoyable. Attendance flexible, grading generous on projects.")
    st.success("**Exam Advice:** Exams can be tough, but other graded work balances it out.")

# Professor: Yue Zhang (cross-listed)
with st.expander("⭐ Professor: Yue Zhang (1 review)", expanded=False):
    st.write("**Review - Solana Anderson (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐⭐ (4/5)")
    st.write("- **Difficulty:** 💪💪💪💪 (4/5)")

st.divider()

# -----------------------------------
# Related Courses
# -----------------------------------
st.subheader("📚 Related Course Reviews")

st.info("**Note:** The following reviews are for related accounting courses (ACCT 2301 and ACCT 3401) and are included for reference.")

# ACCT 2301
with st.expander("📘 ACCT 2301 – Profit Analysis for Managers and Advisors", expanded=False):
    st.write("**Professor: Udi Hoitash**")
    st.write("**Review - Aidan Lothian (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐⭐ (4/5)")
    st.write("- **Difficulty:** 💪 (1/5)")

# ACCT 3401
with st.expander("📘 ACCT 3401 – Financial Reporting and Analysis", expanded=False):
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
    st.write("1. Jeremy Jones (1 review)")
    st.write("2. Anthony Russo (1 review)")
    st.write("3. Yue Zhang (1 review)")

with col2:
    st.write("**Common Themes:**")
    st.write("- Professors balance theory and practice")
    st.write("- Attendance policies are flexible")
    st.write("- Exams can be challenging but projects/assignments help boost grades")
    st.write("- Humor and approachability make classes engaging")

st.divider()

# -----------------------------------
# Study Notes
# -----------------------------------
st.subheader("📂 Available Study Notes")

notes_list = [
    {"title": "Intro to Financial Accounting Concepts", "file": "acct1201_concepts.pdf"},
    {"title": "Journal Entries Practice Set", "file": "journal_entries.docx"},
    {"title": "Financial Statements Cheat Sheet", "file": "financial_statements.pdf"},
    {"title": "Midterm Study Guide", "file": "acct1201_midterm.pdf"},
    {"title": "Final Exam Review Notes", "file": "acct1201_final_review.pdf"},
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
- 📘 [AccountingCoach - Financial Accounting](https://www.accountingcoach.com/financial-accounting/explanation)  
- 🎥 [Financial Accounting Basics Playlist](#)  
- 💼 [Corporate Finance Institute Resources](https://corporatefinanceinstitute.com/)  
- 📊 [Excel for Accountants Tutorial](https://www.youtube.com/watch?v=rwbho0CgEAE)  
- 📈 [Practice Problems – Financial Accounting](https://www.excel-practice-online.com/)
""")
