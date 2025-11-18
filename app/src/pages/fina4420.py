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
st.title("FINA 4420 – Mergers and Acquisitions")
st.write("Welcome, {0} 👋".format(st.session_state.get('first_name', 'Student')))
st.write("Here you can view professor rankings, notes, and useful resources for this course.")
st.divider()

# -----------------------------------
# Course Overview
# -----------------------------------
st.subheader("📊 Course Overview")
col1, col2, col3 = st.columns(3)
with col1: st.metric("Average Enjoyment", "3/5", help="Based on student reviews")
with col2: st.metric("Average Difficulty", "1.3/5", help="Based on student reviews")
with col3: st.metric("Total Reviews", "3", help="Number of student reviews (FINA 4420 only)")
st.divider()

# -----------------------------------
# Professor Reviews
# -----------------------------------
st.subheader("👨‍🏫 Professor Reviews")
with st.expander("⭐ Professor: Ryan Tracey (3 reviews)", expanded=True):
    st.write("**Review - Adhitya Selvaraman (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐ (3/5)")
    st.write("- **Difficulty:** 💪 (1/5)")
    st.info("**Comments:** No additional comments provided.")

    st.write("**Review - Vanessa Jiao (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐ (3/5)")
    st.write("- **Difficulty:** 💪💪 (2/5)")
    st.info("**Comments:** No additional comments provided.")

    st.write("**Review - Jessica Levesque (Fall 2024)**")
    st.write("- **Format:** In Person")
    st.write("- **Enjoyment:** ⭐⭐⭐ (3/5)")
    st.write("- **Difficulty:** 💪 (1/5)")
    st.info("**Comments:** No additional comments provided.")
st.divider()

# -----------------------------------
# Key Takeaways
# -----------------------------------
st.subheader("💡 Key Takeaways from Reviews")
col1, col2 = st.columns(2)
with col1: 
    st.write("**Most Popular Professors:**")
    st.write("1. Ryan Tracey (3 reviews)")
with col2: 
    st.write("**Common Themes:**")
    st.write("- Moderate enjoyment overall")
    st.write("- Difficulty rated low to moderate")
    st.write("- Consistency across reviews suggests approachable course structure")
st.divider()

# -----------------------------------
# Study Notes
# -----------------------------------
st.subheader("📂 Available Study Notes")
notes_list = [
    {"title": "M&A Case Study Guide", "file": "fina4420_cases.pdf"},
    {"title": "Valuation & Deal Structure Notes", "file": "fina4420_valuation.docx"},
    {"title": "Final Exam Review Sheet", "file": "fina4420_final.pdf"},
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
- 📘 [Mergers & Acquisitions Textbook](#)  
- 🎓 [Khan Academy: Corporate Finance & M&A](https://www.khanacademy.org/)  
- 🎥 [YouTube Playlist: M&A Explained](#)  
- 📊 [Practice Problems – Deal Structuring & Valuation](#)  
""")
