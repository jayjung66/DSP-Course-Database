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
# -------------------------------
# Hardcoded list of courses (you can later pull this from DB)
# Each course maps to its page file
# -------------------------------
courses = {
    # Accounting
    "ACCT 1201 - Financial Accounting and Reporting": "pages/acct1201.py",
    
    # Architecture
    "ARCH 1450 - Architecture Course": "pages/arch1450.py",
    
    # Biology
    "BIOL 1147 - Biology Course": "pages/biol1147.py",
    
    # Chemical Engineering
    "CAEP 2290 - Chemical Engineering Course": "pages/caep2290.py",
    
    # Communication
    "CMN 3306 - Communication Course": "pages/cmn3306.py",
    "COMM 1112 - Communication 1": "pages/comm1112.py",
    "COMM 1113 - Communication 2": "pages/comm1113.py",
    "COMM 2650 - Communication Course": "pages/comm2650.py",
    "COMM 3304 - Communication Course": "pages/comm3304.py",
    "COMM 3451 - Communication Course": "pages/comm3451.py",
    "COMM 4464 - Communication Course": "pages/comm4464.py",
    
    # Criminal Justice
    "CRIM 1200 - Criminal Justice": "pages/crim1200.py",
    
    # Computer Science
    "CS 1800 - Discrete Structures": "pages/cs1800.py",
    "CS 2500 - Fundamentals of Computer Science": "pages/cs2500.py",
    
    # Data Science
    "DS 2000 - Data Science": "pages/ds2000.py",
    "DS 2001 - Data Science 2": "pages/ds2001.py",
    "DS 2500 - Data Science Course": "pages/ds2500.py",
    "DS 4300 - Data Science Course": "pages/ds4300.py",
    
    # Economics
    "ECON 1115 - Principles of Macroeconomics": "pages/econ1115.py",
    "ECON 1116 - Principles of Microeconomics": "pages/econ1116.py",
    "ECON 1260 - Economics Course": "pages/econ1260.py",
    
    # Engineering
    "ENGW 3304 - Engineering Writing": "pages/engw3304.py",
    
    # Finance
    "FINA 1209 - Finance Course": "pages/fina1209.py",
    "FINA 2201 - Financial Management": "pages/fina2201.py",
    "FINA 2730 - Finance Course": "pages/fina2730.py",
    "FINA 3301 - Finance Course": "pages/fina3301.py",
    "FINA 3303 - Finance Course": "pages/fina3303.py",
    "FINA 4219 - Finance Course": "pages/fina4219.py",
    "FINA 4335 - Finance Course": "pages/fina4335.py",
    "FINA 4412 - Finance Course": "pages/fina4412.py",
    "FINA 4420 - Finance Course": "pages/fina4420.py",
    "FINA 4512 - Finance Course": "pages/fina4512.py",
    "FINA 4526 - Finance Course": "pages/fina4526.py",
    "FINA 4604 - Finance Course": "pages/fina4604.py",
    
    # Innovation
    "INNO 2414 - Innovation Course": "pages/inno2414.py",
    "INNO 4506 - Innovation Course": "pages/inno4506.py",
    
    # International Business
    "INTB 1203 - International Business": "pages/intb1203.py",
    "INTB 1101 - International Business 2": "pages/intb1101.py",
    
    # Mathematics
    "MATH 2321 - Calculus 3": "pages/math2321.py",
    "MATH 2331 - Linear Algebra": "pages/math2331.py",
    "MATH 2341 - Differential Equations": "pages/math2341.py",
    
    # Management
    "MGMT 3302 - Management Course": "pages/mgmt3302.py",
    "MGMT 4983 - Management Course": "pages/mgmt4983.py",
    
    # MIS
    "MISM 3501 - MIS Course": "pages/mism3501.py",
    
    # Marketing
    "MKTG 2201 - Introduction to Marketing": "pages/mktg2201.py",
    "MKTG 3402 - Marketing Research": "pages/mktg3402.py",
    "MKTG 3720 - Brand Management": "pages/mktg3720.py",
    "MKTG 4504 - Advertising & Brand Promotion": "pages/mktg4504.py",
    
    # Organizational Behavior
    "ORGB 3201 - Organizational Behavior": "pages/orgb3201.py",
    
    # Psychology
    "PSYC 1210 - Introduction to Psychology": "pages/psyc1210.py",
    "PSYC 3452 - Psychology Course": "pages/psyc3452.py",
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
