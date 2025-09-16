import streamlit as st

st.set_page_config(
    page_title=("Assignment Dashboard"),
    page_icon=("📊"),
)

# Sidebar configuration
st.sidebar.image("./assets/project-logo.jpg",)
st.sidebar.success("Select a tab above.")

# # Page information

st.write("# Welcome to my dashboard for Assignment 2 👋")

st.markdown(
"""
This is dashboard shows the probability of stroke between genders using a synthetic data set!
"""
)
import pandas as pd
import numpy as np
import plotly.express as px

st.title("♂️ Stroke Risk by Gender ♀️")

# Synthetic data set ans usign 42 for reproducability
np.random.seed(42)
df = pd.DataFrame({
    "Gender": np.random.choice(["Male","Female"], 500),
    "Stroke": np.random.binomial(1, 0.1, 500)
})

# Compute stroke percentage
risk = df.groupby("Gender")["Stroke"].mean().reset_index()
risk["stroke"] *= 100

#The actual plot
fig = px.bar(risk, x="Gender", y="Stroke", color="Gender",
             color_discrete_map={"Male":"blue","Female":"red"},
             text=risk["Stroke"].round(1))

fig.update_layout(
    yaxis_title="Stroke Risk (%)",
    showlegend=False
)

fig.update_traces(texttemplate="%{text:.1f}%")  #Adds % on top of bars, for more clarity

st.plotly_chart(fig, use_container_width=True)