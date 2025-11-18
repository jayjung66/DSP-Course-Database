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
st.title("ORGB 3201 – Organizational Behavior")
st.write("Welcome, {0} 👋".format(st.session_state.get('first_name', 'Student')))
st.write("Here you can view professor rankings, notes, and useful resources for this course.")
st.divider()

# -----------------------------------
# Course Overview
# -----------------------------------
st.subheader("📊 Course Overview")
col1, col2, col3 = st.columns(3)
with col1: st.metric("Average Enjoyment", "3/5", help="Based on student reviews")
with col2: st.metric("Average Difficulty", "3/5", help="Based on student reviews")
with col3: st.metric("Total Reviews", "5", help="Number of student reviews (ORGB 3201 only)")
st.divider()

# -----------------------------------
# Professor Reviews
# -----------------------------------
st.subheader("👨‍🏫 Professor Reviews")

with st.expander("⭐ Professor: Heather Jean MacNeil (1 review)", expanded=True):
    st.write("**Review - Katie Kerl (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐⭐ (4/5)")
    st.write("- **Difficulty:** 💪💪 (2/5)")
    st.info("**Comments:** Favorite professor I’ve ever had!!")

with st.expander("⭐ Professor: Dee Masielo (1 review)", expanded=False):
    st.write("**Review - Emily Cai (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐ (2/5)")
    st.write("- **Difficulty:** 💪💪💪 (3/5)")
    st.info("**Comments:** Not a fan, professor was chronically late.")

with st.expander("⭐ Professor: Zeynep Aksehirli (2 reviews)", expanded=False):
    st.write("**Review - Chloe Vergel de Dios (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐ (3/5)")
    st.write("- **Difficulty:** 💪💪💪 (3/5)")
    st.info("**Comments:** No additional comments provided.")

    st.write("**Review - Susan Huang (Spring 2025)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐ (2/5)")
    st.write("- **Difficulty:** 💪💪💪 (3/5)")
    st.info("**Comments:** Lectures are a little boring and she can be harsh on grading essays. Exams are specific and include open-ended sections.")

with st.expander("⭐ Professor: Sarah Woodside (1 review)", expanded=False):
    st.write("**Review - Vanessa Jiao (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐⭐ (4/5)")
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
    st.write("1. Heather Jean MacNeil (1 review)")
    st.write("2. Dee Masielo (1 review)")
    st.write("3. Zeynep Aksehirli (2 reviews)")
    st.write("4. Sarah Woodside (1 review)")
with col2:
    st.write("**Common Themes:**")
    st.write("- Experiences vary widely depending on professor")
    st.write("- MacNeil highly praised, very positive experience")
    st.write("- Masielo criticized for lateness")
    st.write("- Aksehirli seen as average to below average, strict grading")
    st.write("- Woodside rated positively but with higher difficulty")
st.divider()

# -----------------------------------
# Study Notes
# -----------------------------------
st.subheader("📂 Available Study Notes")
notes_list = [
    {"title": "Organizational Behavior Case Studies", "file": "orgb3201_cases.pdf"},
    {"title": "Leadership & Team Dynamics Notes", "file": "orgb3201_notes.docx"},
    {"title": "Final Exam Review Sheet", "file": "orgb3201_final.pdf"},
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
- 📘 [Organizational Behavior Textbook](#)  
- 🎓 [Khan Academy: Organizational Behavior Basics](https://www.khanacademy.org/)  
- 🎥 [YouTube Playlist: Organizational Behavior](#)  
- 📊 [Practice Problems – Case Analysis & Team Dynamics](#)  
""")
