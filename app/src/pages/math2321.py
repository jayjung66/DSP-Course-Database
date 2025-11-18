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
st.title("MATH 2321 – Calculus 3 for Science and Engineering")
st.write("Welcome, {0} 👋".format(st.session_state.get('first_name', 'Student')))
st.write("Here you can view professor rankings, notes, and useful resources for this course.")
st.divider()

# -----------------------------------
# Course Overview
# -----------------------------------
st.subheader("📊 Course Overview")
col1, col2, col3 = st.columns(3)
with col1: st.metric("Average Enjoyment", "4/5", help="Based on student reviews")
with col2: st.metric("Average Difficulty", "3.5/5", help="Based on student reviews")
with col3: st.metric("Total Reviews", "2", help="Number of student reviews (MATH 2321 only)")
st.divider()

# -----------------------------------
# Professor Reviews
# -----------------------------------
st.subheader("👨‍🏫 Professor Reviews")

with st.expander("⭐ Professor: Oana Veliche (1 review)", expanded=True):
    st.write("**Review - Krystal Zepaj (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐⭐ (4/5)")
    st.write("- **Difficulty:** 💪💪💪💪 (4/5)")
    st.info("**Comments:** She is ok but you have to teach yourself everything. She does not know how to teach. Final exam is horrible but her exams were somewhat predictable.")

with st.expander("⭐ Professor: Sumi Seo (1 review)", expanded=False):
    st.write("**Review - Shrey Patel (Spring 2025)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐⭐ (4/5)")
    st.write("- **Difficulty:** 💪💪💪 (3/5)")
    st.info("**Comments:** Great professor for calc imo, can go fast sometimes but good lecturer. No homework but weekly quizzes. Exams are 80% of the grade but she provides good study materials.")
st.divider()

# -----------------------------------
# Key Takeaways
# -----------------------------------
st.subheader("💡 Key Takeaways from Reviews")
col1, col2 = st.columns(2)
with col1:
    st.write("**Most Popular Professors:**")
    st.write("1. Oana Veliche (1 review)")
    st.write("2. Sumi Seo (1 review)")
with col2:
    st.write("**Common Themes:**")
    st.write("- Exams are a major component of grading")
    st.write("- Veliche’s teaching style requires self-study")
    st.write("- Seo praised as a strong lecturer, though fast-paced")
    st.write("- Moderate to high difficulty overall")
st.divider()

# -----------------------------------
# Study Notes
# -----------------------------------
st.subheader("📂 Available Study Notes")
notes_list = [
    {"title": "Multivariable Calculus Notes", "file": "math2321_multivariable.pdf"},
    {"title": "Vector Calculus & Applications", "file": "math2321_vectors.docx"},
    {"title": "Final Exam Review Sheet", "file": "math2321_final.pdf"},
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
- 📘 [Calculus 3 Textbook](#)  
- 🎓 [Khan Academy: Multivariable Calculus](https://www.khanacademy.org/)  
- 🎥 [YouTube Playlist: Calculus 3 Explained](#)  
- 📊 [Practice Problems – Gradient, Divergence, Curl](#)  
""")
