import streamlit as st

st.set_page_config(
    page_title=("Assignment Dashboard"),
    page_icon=("📊"),
)

# Sidebar configuration
st.sidebar.image("./assets/project-logo.jpg",)
st.sidebar.success("Select a tab above.")

# The main page
st.set_page_config(page_title="📊 Dashboard", page_icon="📊")

st.title("📊 Dashboard")

# Page navigation
st.page_link("Dashboard.py", label="🏠 Dashboard")
st.page_link("pages/About.py", label="ℹ️ About")

#The 2nd page
st.set_page_config(page_title="ℹ️ About", page_icon="ℹ️")

st.title("ℹ️ About Page")

# Page navigation
st.page_link("Dashboard.py", label="🏠 Dashboard")
st.page_link("pages/About.py", label="ℹ️ About")

# # Page information

st.write("# Welcome to my dashboard for Assignment 2 👋")

st.markdown(
"""
    ## Aims

    After completing the course the student should be able to:
    - explain basic project management methods
    - be able to account for success factors in Health Informatics projects
    - understand basic methods and tools in the field of data science and machine learning
    - explain process models for data mining projects
    - explain the difference between rule-based methods and machine learning methods
    - apply basic project management methods
    - work in an international multidisciplinary project group
    - independently lead and implement a limited project in health informatics - document the steps in the design of a prototype for a health informatics project
    - apply the steps in a process model for data mining projects
    - apply methods from the field of text mining on different types of health informatics problems
    - explain and argue for their positions regarding the implementation of a health informatics project
    - explain how to work with sensitive health information in a safe and ethical way.

"""
)

# You can also add text right into the web as long comments (""")
"""
The final project aims to apply data science concepts and skills on a 
medical case study that you and your team select from a public data source.
The project assumes that you bring the technical Python skills from 
previous courses (*DSHI*: Data Science for Health Informatics), as well as 
the analytical skills to argue how and why specific techniques could
enhance the problem domain related to the selected dataset.
"""

### UNCOMMENT THE CODE BELOW TO SEE EXAMPLE OF INPUT WIDGETS

# # DATAFRAME MANAGEMENT
import numpy as np

dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)

# # Add a slider to the sidebar:
add_slider = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)
