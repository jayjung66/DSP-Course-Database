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
st.title("MKTG 4504 – Advertising and Brand Promotion")
st.write("Welcome, {0} 👋".format(st.session_state.get('first_name', 'Student')))
st.write("Here you can view professor rankings, notes, and useful resources for this course.")
st.divider()

# -----------------------------------
# Course Overview
# -----------------------------------
st.subheader("📊 Course Overview")
col1, col2, col3 = st.columns(3)
with col1: st.metric("Average Enjoyment", "2.8/5", help="Based on student reviews")
with col2: st.metric("Average Difficulty", "4/5", help="Based on student reviews")
with col3: st.metric("Total Reviews", "5", help="Number of student reviews (MKTG 4504 only)")
st.divider()

# -----------------------------------
# Professor Reviews
# -----------------------------------
st.subheader("👨‍🏫 Professor Reviews")

with st.expander("⭐ Professor: Rachel Stewart (5 reviews)", expanded=True):
    st.write("**Review - Katie Kerl (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐⭐ (4/5)")
    st.write("- **Difficulty:** 💪💪💪💪 (4/5)")
    st.info("**Comments:** Was a rough semester for her, not a bad person at all just a tough grader!")

    st.write("**Review - Ty Orlando (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐ (2/5)")
    st.write("- **Difficulty:** 💪💪 (2/5)")
    st.info("**Comments:** No additional comments provided.")

    st.write("**Review - Tavish Nunes (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐ (3/5)")
    st.write("- **Difficulty:** 💪💪💪💪 (4/5)")
    st.info("**Comments:** Not very hard work, just a toooooon for no reason.")

    st.write("**Review - Chloe Vergel de Dios (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐ (3/5)")
    st.write("- **Difficulty:** 💪💪💪💪💪 (5/5)")
    st.info("**Comments:** No additional comments provided.")

    st.write("**Review - Audrey McGuff (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐ (2/5)")
    st.write("- **Difficulty:** 💪💪💪💪💪 (5/5)")
    st.info("**Comments:** No additional comments provided.")
st.divider()

# -----------------------------------
# Key Takeaways
# -----------------------------------
st.subheader("💡 Key Takeaways from Reviews")
col1, col2 = st.columns(2)
with col1:
    st.write("**Most Popular Professors:**")
    st.write("1. Rachel Stewart (5 reviews)")
with col2:
    st.write("**Common Themes:**")
    st.write("- Heavy workload, sometimes perceived as excessive")
    st.write("- Difficulty consistently rated high (4–5)")
    st.write("- Enjoyment varies widely (2–4)")
    st.write("- Stewart is seen as tough but fair, grading can feel strict")
st.divider()

# -----------------------------------
# Study Notes
# -----------------------------------
st.subheader("📂 Available Study Notes")
notes_list = [
    {"title": "Advertising & Promotion Case Studies", "file": "mktg4504_cases.pdf"},
    {"title": "Brand Promotion Strategies Notes", "file": "mktg4504_notes.docx"},
    {"title": "Final Exam Review Sheet", "file": "mktg4504_final.pdf"},
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
- 📘 [Advertising & Brand Promotion Textbook](#)  
- 🎓 [Khan Academy: Marketing & Promotion Basics](https://www.khanacademy.org/)  
- 🎥 [YouTube Playlist: Advertising & Brand Promotion](#)  
- 📊 [Practice Problems – Campaign Design & Case Analysis](#)  
""")
