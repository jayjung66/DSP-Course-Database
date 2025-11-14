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
st.title("FINA 2201 – Financial Management")
st.write("Welcome, {0} 👋".format(st.session_state.get('first_name', 'Student')))
st.write("Here you can view professor rankings, notes, and useful resources for this course.")

st.divider()

# -----------------------------------
# Course Overview
# -----------------------------------
st.subheader("📊 Course Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Average Enjoyment", "3.6/5", help="Based on student reviews")

with col2:
    st.metric("Average Difficulty", "3.1/5", help="Based on student reviews")

with col3:
    st.metric("Total Reviews", "7", help="Number of student reviews")

st.divider()

# -----------------------------------
# Professor Reviews
# -----------------------------------
st.subheader("👨‍🏫 Professor Reviews")

# Professor: Saptarshi Mukherjee (3 reviews)
with st.expander("⭐ Professor: Saptarshi Mukherjee (3 reviews)", expanded=True):
    st.write("**Review #1 - Aidan Lothian (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐⭐ (4/5)")
    st.write("- **Difficulty:** 💪💪💪💪 (4/5)")
    st.info("**Comments:** Mukherjee is literally the nicest guy ever ever. He has a policy where if you complete all assignments you automatically get a B. Super easy to get points from him. He does have a 10% participation grade even though it is a lecture, so make sure to make an effort to raise your hand every now and then. I would heavily recommend taking the time to ask him questions after class so that he knows your face and name.")
    st.success("**Exam Advice:** All tests in his class are online on the computer with no lockdown browser... all I have to say. Exams are tough tbh if you are taking them honestly. He will typically have a curve.")
    
    st.write("")
    st.write("**Review #2 - Abigail DeMaioribus (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐⭐ (4/5)")
    st.write("- **Difficulty:** 💪💪💪 (3/5)")
    
    st.write("")
    st.write("**Review #3 - Sarah Bouvier (Fall 2023)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐ (3/5)")
    st.write("- **Difficulty:** 💪💪 (2/5)")
    st.info("**Comments:** He is really sweet. All the homeworks and most exam questions (NOT THE FINAL) are online. I didn't really feel like I learned much the whole semester though. He was very inconsistent where all the homework questions were from Chegg and solved completely differently than what we learned in class. Because all the answers are online, it can be hard to get an A since everyone gets very similar grades on most assignments.")
    st.success("**Exam Advice:** Take the exams in groups and don't be the first one to start it. Usually the solutions pop up right after you submit.")

# Professor: Jack Mazur
with st.expander("⭐ Professor: Jack Mazur (1 review)", expanded=False):
    st.write("**Review - Leo Harmon (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐⭐ (4/5)")
    st.write("- **Difficulty:** 💪💪 (2/5)")
    st.info("**Comments:** LOVE HIM. looks like he was born in fenway park. thick boston accent but thicker heart. doesn't use presentations in class and kind of rambles so you have to pay attention but is always there for help and explains things very easily. expects a lot of participation and you can't be late/absent to class. recommend tho. pretty easy.")

# Professor: Sunayan Acharya
with st.expander("⭐ Professor: Sunayan Acharya (1 review)", expanded=False):
    st.write("**Review - Sylvia Dunaevschi (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐ (2/5)")
    st.write("- **Difficulty:** 💪💪💪💪 (4/5)")
    st.info("**Comments:** Good at teaching and will provide help if you come into OH. Difficult exams and no curve typically.")

# Professor: Mark Gooley
with st.expander("⭐ Professor: Mark Gooley (1 review)", expanded=False):
    st.write("**Review - Vikram Subramanyam (Summer 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐⭐⭐ (5/5)")
    st.write("- **Difficulty:** 💪💪💪 (3/5)")

# Professor: Tian Tian Gu
with st.expander("⭐ Professor: Tian Tian Gu (1 review)", expanded=False):
    st.write("**Review - Chloe Tu (Spring 2025)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐ (3/5)")
    st.write("- **Difficulty:** 💪💪💪💪 (4/5)")
    st.info("**Comments:** Prof is super sweet but she goes super fast after the first chapter and it's hard to keep up. Her exams are more like the extra practice problems she gives you which are a lot harder but exams are online and are taken at home. There's a code for attendance so it's technically mandatory to go to class. She is also super understanding though, and if you need to go to a different sections class or take the exam during the other section's time she'll let you.")
    st.success("**Exam Advice:** Yes; both midterms are online, final is online as well but you get proctored in person. They also have no lock down browser or camera for all the exams.")

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

with col2:
    st.write("**Common Themes:**")
    st.write("- Most exams are online")
    st.write("- No lockdown browser typically")
    st.write("- Curves often applied")
    st.write("- Participation expected")

st.divider()

# -----------------------------------
# Study Notes
# -----------------------------------
st.subheader("📂 Available Study Notes")

notes_list = [
    {"title": "Time Value of Money Guide", "file": "tvm_guide.pdf"},
    {"title": "Financial Ratios Cheat Sheet", "file": "financial_ratios.pdf"},
    {"title": "Capital Budgeting Notes", "file": "capital_budgeting.docx"},
    {"title": "Midterm Review Package", "file": "midterm_review.pdf"},
    {"title": "Final Exam Formula Sheet", "file": "final_formulas.pdf"},
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
- 📊 [Financial Calculator Tutorial](#)  
- 🎥 [Corporate Finance YouTube Playlist](#)  
- 📘 [Investopedia Financial Management](https://www.investopedia.com/terms/f/financial-management.asp)  
- 💰 [Khan Academy: Finance & Capital Markets](https://www.khanacademy.org/economics-finance-domain/core-finance)
- 📈 [Yahoo Finance](https://finance.yahoo.com/)
""")