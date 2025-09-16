import streamlit as st

st.set_page_config(
    page_title=("Assignment Dashboard"),
    page_icon=("📊"),
)

# Sidebar configuration
st.sidebar.image("./assets/project-logo.jpg",)
st.sidebar.success("Select a tab above.")

# The main page


# # Page information

st.write("# Welcome to my dashboard for Assignment 2 👋")

st.markdown(
"""
This is an example dashboard on risk management of having a stroke. This Dashboard uses a synthetic database.
"""
)
import pandas as pd
import numpy as np

np.random.seed(42) #Seed in 42 to make it reproducable
n = 500
df = pd.DataFrame({
    "gender": np.random.choice(["Male","Female"], n),
    "stroke": np.random.binomial(1, 0.1, n) #Makes it random
})

#Calculate stroke percentage by gender
risk = df.groupby("gender")["stroke"].mean() * 100

#Show bar chart
st.bar_chart(risk)

#Show table
st.dataframe(risk.round(1))