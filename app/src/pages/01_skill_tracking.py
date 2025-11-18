import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')

# Sidebar
SideBarLinks()

# Back button
if st.button("⬅️ Back to Course Page"):
    st.switch_page('pages/ECON1116.py')  # replace with your course page file name

# Fetch all available skills
def fetch_all_professors():
    try:
        response = requests.get(f"{API_BASE}/skills/all")
        response.raise_for_status()
        return response.json()  # Parse JSON response
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching students: {e}")
        return []
# -----------------------------------
# Page Content
# -----------------------------------
st.title("✍️ Rate a Professor – ECON 1116")

st.write("Please provide your rating for professors teaching **Principles of Microeconomics (ECON 1116)**.")

# List of professors (could come from DB later)
professors = ["Prof. Johnson", "Prof. Lee", "Prof. Patel", "Prof. Hernandez", "Prof. Smith"]

# Select professor
selected_prof = st.selectbox("Select a Professor", professors)

st.divider()

# Rating categories
st.subheader(f"Rate {selected_prof}")
clarity = st.slider("Clarity of Lectures", 1, 5, 3)
engagement = st.slider("Class Engagement", 1, 5, 3)
fairness = st.slider("Grading Fairness", 1, 5, 3)
helpfulness = st.slider("Helpfulness Outside Class", 1, 5, 3)

# Notes/comments
note = st.text_area("Additional Comments (optional)", placeholder="Write your thoughts here...")

# Submit button
if st.button("✅ Submit Rating", type="primary", use_container_width=True):
    # For now, just display confirmation
    st.success(f"Thank you! Your rating for {selected_prof} has been submitted.")
    
    # Log submission
    logger.info(f"Rating submitted for {selected_prof}: "
                f"Clarity={clarity}, Engagement={engagement}, Fairness={fairness}, Helpfulness={helpfulness}, Note={note}")

    # TODO: Save to database or file
