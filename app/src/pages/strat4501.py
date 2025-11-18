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
st.title("STRT 4501 – Strategy in Action")
st.write("Welcome, {0} 👋".format(st.session_state.get('first_name', 'Student')))
st.write("Here you can view professor rankings, notes, and useful resources for this course.")
st.divider()

# -----------------------------------
# Course Overview
# -----------------------------------
st.subheader("📊 Course Overview")
col1, col2, col3 = st.columns(3)
with col1: st.metric("Average Enjoyment", "2.75/5", help="Based on student reviews")
with col2: st.metric("Average Difficulty", "3/5", help="Based on student reviews")
with col3: st.metric("Total Reviews", "4", help="Number of student reviews (STRT 4501 only)")
st.divider()

# -----------------------------------
# Professor Reviews
# -----------------------------------
st.subheader("👨‍🏫 Professor Reviews")

with st.expander("⭐ Professor: Anna Lamin (1 review)", expanded=True):
    st.write("**Review - Adhitya Selvaraman (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐ (2/5)")
    st.write("- **Difficulty:** 💪💪 (2/5)")
    st.info("**Comments:** No additional comments provided.")

with st.expander("⭐ Professor: Elizabeth Moore (1 review)", expanded=False):
    st.write("**Review - Emily Miller (Fall 2024)**")
    st.write("- **Format:** Online")
    st.write("- **Enjoyment:** ⭐⭐⭐ (3/5)")
    st.write("- **Difficulty:** 💪💪💪💪 (4/5)")
    st.info("**Comments:** This was an online class so it felt like busy work that was graded harshly. I did enjoy the content, it just wasn’t as enjoyable in a class setting. This class was sneaky hard. The tests were completely out of left field so even when I studied and knew the content I did poorly.")

with st.expander("⭐ Professor: Larissa Marchiori Pacheco (1 review)", expanded=False):
    st.write("**Review - Rachel Song (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐ (2/5)")
    st.write("- **Difficulty:** 💪💪 (2/5)")
    st.info("**Comments:** No additional comments provided.")

with st.expander("⭐ Professor: Anna Lamina (1 review)", expanded=False):
    st.write("**Review - Rada Wiratyosin (Fall 2024)**")
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
    st.write("1. Anna Lamin (1 review)")
    st.write("2. Elizabeth Moore (1 review)")
    st.write("3. Larissa Marchiori Pacheco (1 review)")
    st.write("4. Anna Lamina (1 review)")
with col2:
    st.write("**Common Themes:**")
    st.write("- Mixed enjoyment ratings (2–4)")
    st.write("- Difficulty varies from easy (2) to challenging (4)")
    st.write("- Online format (Moore) felt like busy work and was graded harshly")
    st.write("- In-person classes vary widely depending on professor")
    st.write("- Tests can be unpredictable and tough")
st.divider()

# -----------------------------------
# Study Notes
# -----------------------------------
st.subheader("📂 Available Study Notes")
notes_list = [
    {"title": "Strategy in Action Case Studies", "file": "strt4501_cases.pdf"},
    {"title": "Strategic Management Notes", "file": "strt4501_notes.docx"},
    {"title": "Final Exam Review Sheet", "file": "strt4501_final.pdf"},
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
- 📘 [Strategic Management Textbook](#)  
- 🎓 [Khan Academy: Business Strategy Basics](https://www.khanacademy.org/)  
- 🎥 [YouTube Playlist: Strategy in Action](#)  
- 📊 [Practice Problems – Strategic Case Analysis](#)  
""")
