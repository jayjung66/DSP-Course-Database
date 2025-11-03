##################################################
# This is the main/entry-point file for the 
# sample application for your project
##################################################

# Set up basic logging infrastructure
import logging
logging.basicConfig(format='%(filename)s:%(lineno)s:%(levelname)s -- %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# import the main streamlit library as well
# as SideBarLinks function from src/modules folder
import streamlit as st
from modules.nav import SideBarLinks

# streamlit supports regular and wide layout
st.set_page_config(layout='wide')

# Not authenticated at this page
st.session_state['authenticated'] = False

# Sidebar links
SideBarLinks(show_home=True)

# ***************************************************
#    The major content of this page
# ***************************************************
logger.info("Loading the Home page of the app")
st.title('Delta Sigma Pi Sigma Omega Database')
st.write('\n\n')
st.write('### Search for Courses')

# -------------------------------
# Hardcoded list of courses (you can later pull this from DB)
# Each course maps to its page file
# -------------------------------
courses = {
    "FINA 2201 - Financial Management": "pages/fina2201.py",
    "ACCT 1201 - Financial Accounting and Reporting": "pages/acct1201.py",
    "MATH 1342 - Calculus 2": "pages/03_skill_management.py",
    "PHYS 1151 - Physics 1": "pages/03_skill_management.py",
    "PHYS 1152 - Physics 2": "pages/03_skill_management.py",
    "ECON 1115 - Principles of Macroeconomics": "pages/econ1115.py",
    "ECON 1116 - Principles of Microeconomics": "pages/03_skill_management.py",
    "BUSN 1101 - Introduction to Business": "pages/03_skill_management.py"
}

# -------------------------------
# Search bar
# -------------------------------
search_query = st.text_input("🔎 Enter course name or code")

if search_query:
    # filter results
    results = {c: page for c, page in courses.items() if search_query.lower() in c.lower()}
    
    if results:
        st.subheader("Results:")
        for course, page in results.items():
            if st.button(course, use_container_width=True):
                st.session_state['authenticated'] = True
                st.session_state['role'] = 'student'
                st.session_state['first_name'] = 'Alex'
                st.session_state['selected_course'] = course
                logger.info(f"User selected course: {course}, routing to {page}")
                st.switch_page(page)
    else:
        st.info("No matching courses found.")
else:
    st.write("Type above to search courses.")

# -------------------------------
# "My Classes" button
# -------------------------------
st.write("---")
if st.button("📚 My Classes", use_container_width=True):
    st.switch_page("pages/02_skill_gap_analysis.py")