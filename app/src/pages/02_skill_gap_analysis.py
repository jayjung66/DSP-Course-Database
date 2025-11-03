import streamlit as st

st.set_page_config(layout='wide')

st.title("📚 My Classes")

# -------------------------------
# Hardcoded course catalog
# -------------------------------
available_courses = {
    "ECON 1116 - Principles of Microeconomics": "app/src/pages/00_Student_Home.py",
    "ECON 1115 - Principles of Macroeconomics": "app/src/pages/econ1115.py",
    "CS 2500 - Fundamentals of Computer Science": "pages/CS2500.py",
    "FINA 2201 - Financial Management": "pages/FINA2201.py",
    "MATH 1341 - Calculus 1": "pages/MATH1341.py"
}

# -------------------------------
# Initialize session state
# -------------------------------
if "my_classes" not in st.session_state:
    st.session_state.my_classes = []

# -------------------------------
# Add classes
# -------------------------------
st.subheader("➕ Add Classes")
for course, page in available_courses.items():
    if course not in st.session_state.my_classes:
        if st.button(f"Add {course}", key=f"add_{course}"):
            st.session_state.my_classes.append(course)

# -------------------------------
# Show & manage "My Classes"
# -------------------------------
st.subheader("📂 My Classes")
if st.session_state.my_classes:
    for course in st.session_state.my_classes:
        col1, col2 = st.columns([4,1])
        with col1:
            if st.button(course, key=f"open_{course}"):
                # Redirect to the right course page
                st.switch_page(available_courses[course])
        with col2:
            if st.button("❌ Remove", key=f"remove_{course}"):
                st.session_state.my_classes.remove(course)
else:
    st.info("You haven’t added any classes yet.")
