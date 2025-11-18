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
st.title("FINA 3303 – Investments")
st.write("Welcome, {0} 👋".format(st.session_state.get('first_name', 'Student')))
st.write("Here you can view professor rankings, notes, and useful resources for this course.")
st.divider()

# -----------------------------------
# Course Overview
# -----------------------------------
st.subheader("📊 Course Overview")
col1, col2, col3 = st.columns(3)
with col1: st.metric("Average Enjoyment", "4/5", help="Based on student reviews")
with col2: st.metric("Average Difficulty", "3.2/5", help="Based on student reviews")
with col3: st.metric("Total Reviews", "5", help="Number of student reviews (FINA 3303 only)")
st.divider()

# -----------------------------------
# Professor Reviews
# -----------------------------------
st.subheader("👨‍🏫 Professor Reviews")

# Professor: Joseph Marks
with st.expander("⭐ Professor: Joseph Marks (3 reviews)", expanded=True):
    st.write("**Review - Vikram Subramanyam (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐⭐⭐ (5/5)")
    st.write("- **Difficulty:** 💪💪💪💪 (4/5)")
    st.info("**Comments:** No additional comments provided.")

    st.write("**Review - Sarah Bouvier (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐⭐⭐ (5/5)")
    st.write("- **Difficulty:** 💪💪💪 (3/5)")
    st.info("**Comments:** I cannot recommend him enough. Down to earth, personable, funny, and explains concepts well. Exams require a lot of studying, but you get half a sheet for formulas/notes. Challenging but rewarding.")

    st.write("**Review - Emily Cai (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐⭐⭐ (5/5)")
    st.write("- **Difficulty:** 💪💪💪 (3/5)")
    st.info("**Comments:** Professor is very thorough. Highly recommend.")

# Professor: Cao Fang
with st.expander("⭐ Professor: Cao Fang (1 review)", expanded=False):
    st.write("**Review - Susan Huang (Spring 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐⭐ (4/5)")
    st.write("- **Difficulty:** 💪💪 (2/5)")
    st.info("**Comments:** No additional comments provided.")

# Professor: Da Huang
with st.expander("⭐ Professor: Da Huang (1 review)", expanded=False):
    st.write("**Review - Luke Noble (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐ (1/5)")
    st.write("- **Difficulty:** 💪💪💪💪 (4/5)")
    st.info("**Comments:** No additional comments provided.")
st.divider()

# -----------------------------------
# Key Takeaways
# -----------------------------------
st.subheader("💡 Key Takeaways from Reviews")
col1, col2 = st.columns(2)
with col1:
    st.write("**Most Popular Professors:**")
    st.write("1. Joseph Marks (3 reviews)")
    st.write("2. Cao Fang (1 review)")
    st.write("3. Da Huang (1 review)")
with col2:
    st.write("**Common Themes:**")
    st.write("- Joseph Marks highly praised for clarity, humor, and thoroughness")
    st.write("- Exams often challenging, require significant studying")
    st.write("- Some professors rated easier (Cao Fang) or harder (Da Huang)")
    st.write("- Overall enjoyment generally high except one negative experience")
st.divider()

# -----------------------------------
# Study Notes
# -----------------------------------
st.subheader("📂 Available Study Notes")
notes_list = [
    {"title": "Investments Exam Formula Sheet", "file": "fina3303_formulas.pdf"},
    {"title": "Equity & Fixed Income Notes", "file": "fina3303_equity.docx"},
    {"title": "Final Exam Review Sheet", "file": "fina3303_final.pdf"},
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
- 📘 [Investments Textbook](#)  
- 🎓 [Khan Academy: Investing Basics](https://www.khanacademy.org/)  
- 🎥 [YouTube Playlist: Investments & Portfolio Management](#)  
- 📊 [Practice Problems – Risk & Return Analysis](#)  
""")
