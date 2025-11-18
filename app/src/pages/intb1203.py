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
st.title("INTB 1203 – International Business and Global Social Responsibility")
st.write("Welcome, {0} 👋".format(st.session_state.get('first_name', 'Student')))
st.write("Here you can view professor rankings, notes, and useful resources for this course.")
st.divider()

# -----------------------------------
# Course Overview
# -----------------------------------
st.subheader("📊 Course Overview")
col1, col2, col3 = st.columns(3)
with col1: st.metric("Average Enjoyment", "3.7/5", help="Based on student reviews")
with col2: st.metric("Average Difficulty", "3/5", help="Based on student reviews")
with col3: st.metric("Total Reviews", "3", help="Number of student reviews (INTB 1203 only)")
st.divider()

# -----------------------------------
# Professor Reviews
# -----------------------------------
st.subheader("👨‍🏫 Professor Reviews")

# Professor: Sheila Puffer
with st.expander("⭐ Professor: Sheila Puffer (1 review)", expanded=True):
    st.write("**Review - Leo Harmon (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐ (2/5)")
    st.write("- **Difficulty:** 💪💪💪💪 (4/5)")
    st.info("**Comments:** Prof. Puffer is passionate and loves her work but expects heavy student investment. Two online exams averaged ~65%. Exams were extremely hard, curve applied but evaluation felt unfair. Not recommended.")

# Professor: Gastón de los Reyes
with st.expander("⭐ Professor: Gastón de los Reyes (1 review)", expanded=False):
    st.write("**Review - Joao Andrade Merjam (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐⭐ (4/5)")
    st.write("- **Difficulty:** 💪💪💪 (3/5)")
    st.info("**Comments:** Similar to intro to international business. Professor emphasizes law and older economists. Homework can be heavy before class, but he is very understanding.")

# Professor: Christopher Robertson
with st.expander("⭐ Professor: Christopher Robertson (1 review)", expanded=False):
    st.write("**Review - Solana Anderson (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐⭐⭐ (5/5)")
    st.write("- **Difficulty:** 💪💪 (2/5)")
    st.info("**Comments:** No additional comments provided.")
st.divider()

# -----------------------------------
# Key Takeaways
# -----------------------------------
st.subheader("💡 Key Takeaways from Reviews")
col1, col2 = st.columns(2)
with col1:
    st.write("**Most Popular Professors:**")
    st.write("1. Sheila Puffer (1 review)")
    st.write("2. Gastón de los Reyes (1 review)")
    st.write("3. Christopher Robertson (1 review)")
with col2:
    st.write("**Common Themes:**")
    st.write("- Difficulty varies widely by professor")
    st.write("- Puffer’s exams are very challenging")
    st.write("- De los Reyes emphasizes law and economics readings")
    st.write("- Robertson rated highly enjoyable and easier")
st.divider()

# -----------------------------------
# Study Notes
# -----------------------------------
st.subheader("📂 Available Study Notes")
notes_list = [
    {"title": "Global Social Responsibility Case Studies", "file": "intb1203_cases.pdf"},
    {"title": "International Business Law Readings", "file": "intb1203_law.docx"},
    {"title": "Final Exam Review Sheet", "file": "intb1203_final.pdf"},
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
- 📘 [International Business Textbook](#)  
- 🎓 [Khan Academy: Globalization & Business](https://www.khanacademy.org/)  
- 🎥 [YouTube Playlist: International Business & Social Responsibility](#)  
- 📊 [Practice Problems – Case Analysis on Global Responsibility](#)  
""")
