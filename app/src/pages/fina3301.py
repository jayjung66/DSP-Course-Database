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
st.title("FINA 3301 – Corporate Finance")
st.write("Welcome, {0} 👋".format(st.session_state.get('first_name', 'Student')))
st.write("Here you can view professor rankings, notes, and useful resources for this course.")
st.divider()

# -----------------------------------
# Course Overview
# -----------------------------------
st.subheader("📊 Course Overview")
col1, col2, col3 = st.columns(3)
with col1: st.metric("Average Enjoyment", "2.7/5", help="Based on student reviews")
with col2: st.metric("Average Difficulty", "3.7/5", help="Based on student reviews")
with col3: st.metric("Total Reviews", "3", help="Number of student reviews (FINA 3301 only)")
st.divider()

# -----------------------------------
# Professor Reviews
# -----------------------------------
st.subheader("👨‍🏫 Professor Reviews")
with st.expander("⭐ Professor: Joseph (Joe) Henry (3 reviews)", expanded=True):
    st.write("**Review - Anjalika Shah (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐ (3/5)")
    st.write("- **Difficulty:** 💪💪💪💪 (4/5)")
    st.info("**Comments:** No additional comments provided.")

    st.write("**Review - Joao Andrade Merjam (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐ (3/5)")
    st.write("- **Difficulty:** 💪💪💪 (3/5)")
    st.info("**Comments:** Class was at times boring as he just read off slides. Very knowledgeable, so asking questions helps. No midterms or finals, but two quick and intense quizzes. Toward the end, he added more Excel examples with company analysis, so the class may have changed.")

    st.write("**Review - Caroline Belanger (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐ (2/5)")
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
    st.write("1. Joseph (Joe) Henry (3 reviews)")
with col2:
    st.write("**Common Themes:**")
    st.write("- Exams replaced by quizzes")
    st.write("- Teaching style often slide-based, can feel boring")
    st.write("- Knowledgeable professor, participation helps")
    st.write("- Difficulty rated moderate to high")
    st.write("- Some Excel and applied company analysis introduced")
st.divider()

# -----------------------------------
# Study Notes
# -----------------------------------
st.subheader("📂 Available Study Notes")
notes_list = [
    {"title": "Corporate Finance Quiz Prep Guide", "file": "fina3301_quizprep.pdf"},
    {"title": "Excel Applications in Finance", "file": "fina3301_excel.docx"},
    {"title": "Final Project Review Sheet", "file": "fina3301_final.pdf"},
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
- 🎓 [Khan Academy: Corporate Finance Basics](https://www.khanacademy.org/)  
- 🎥 [YouTube Playlist: Corporate Finance Explained](#)  
- 📊 [Practice Problems – Capital Structure & Valuation](#)  
""")
