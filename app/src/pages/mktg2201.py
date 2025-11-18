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
st.title("MKTG 2201 – Introduction to Marketing")
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
with col3: st.metric("Total Reviews", "5", help="Number of student reviews (MKTG 2201 only)")
st.divider()

# -----------------------------------
# Professor Reviews
# -----------------------------------
st.subheader("👨‍🏫 Professor Reviews")

with st.expander("⭐ Professor: Rachel Stewart (1 review)", expanded=True):
    st.write("**Review - Vikram Subramanyam (Fall 2023)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐⭐ (4/5)")
    st.write("- **Difficulty:** 💪💪💪 (3/5)")
    st.info("**Comments:** No additional comments provided.")

with st.expander("⭐ Professor: Sean Gallagher (2 reviews)", expanded=False):
    st.write("**Review - Chloe Tu (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐⭐ (4/5)")
    st.write("- **Difficulty:** 💪💪 (2/5)")
    st.info("**Comments:** Class itself is super easy; textbook heavy though you have to read the chapter before because you discuss it in class and he is heavy on participation. Quizzes were online using Respondus Lockdown Browser from Fri–Sun afternoon but super chill. You did have to turn on your camera and audio for them, but your last quiz is technically your final which is nice. He also curves the quizzes depending on how your class does. Make sure you do well on your market simulation group project.")

    st.write("**Review - Sarah Bouvier (Fall 2023)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐ (3/5)")
    st.write("- **Difficulty:** 💪💪💪 (3/5)")
    st.info("**Comments:** He is annoying. He will single people out. The class isn't super hard though. I wouldn't really recommend but you'll be fine taking it with him. Get on his good side and participate (all you need to do is read definitions out of the textbook). He scales grades in a weird way. Group project is 30% of your grade.")

with st.expander("⭐ Professor: Robert Durant (1 review)", expanded=False):
    st.write("**Review - Solana Anderson (Spring 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐ (1/5)")
    st.write("- **Difficulty:** 💪💪💪💪 (4/5)")
    st.info("**Comments:** No additional comments provided.")

with st.expander("⭐ Professor: Angela Chang (1 review)", expanded=False):
    st.write("**Review - Andrew Acosta (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐ (3/5)")
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
    st.write("1. Rachel Stewart (1 review)")
    st.write("2. Sean Gallagher (2 reviews)")
    st.write("3. Robert Durant (1 review)")
    st.write("4. Angela Chang (1 review)")
with col2:
    st.write("**Common Themes:**")
    st.write("- Enjoyment varies widely by professor")
    st.write("- Gallagher’s class easier but participation heavy and textbook-focused")
    st.write("- Stewart moderate difficulty, positive experience")
    st.write("- Durant rated very low enjoyment, high difficulty")
    st.write("- Chang moderate enjoyment, relatively easy difficulty")
    st.write("- Group project is a significant grade component")
st.divider()

# -----------------------------------
# Study Notes
# -----------------------------------
st.subheader("📂 Available Study Notes")
notes_list = [
    {"title": "Marketing Principles Notes", "file": "mktg2201_notes.pdf"},
    {"title": "Case Studies in Marketing", "file": "mktg2201_cases.docx"},
    {"title": "Final Exam Review Sheet", "file": "mktg2201_final.pdf"},
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
- 📘 [Marketing Textbook](#)  
- 🎓 [Khan Academy: Marketing Basics](https://www.khanacademy.org/)  
- 🎥 [YouTube Playlist: Introduction to Marketing](#)  
- 📊 [Practice Problems – Market Simulation & Case Analysis](#)  
""")
