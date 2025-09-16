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

import plotly.express as px

st.title("Stroke Risk by Gender")

#Synthetic data set
np.random.seed(42)
df = pd.DataFrame({
    "Gender": np.random.choice(["Male","Female"], 500),
    "Stroke": np.random.binomial(1, 0.1, 500)
})

#Calculating the stroke risk between the genders
risk = df.groupby("Gender")["Stroke"].mean().reset_index()  # keep 0-1

#Shows teh data table
st.subheader("Stroke Risk Data")
st.dataframe(risk.assign(stroke_percent=(risk["Stroke"]*100).round(1)))

#The chart
colors = {"Male":"blue","Female":"red"}
fig = px.bar(risk, x="Gender", y="Stroke", color="Gender",
             color_discrete_map=colors,
             text=risk["Stroke"].round(3))
fig.update_layout(
    yaxis_title="Stroke Risk (%)",
    yaxis_tickformat="%",
    showlegend=False
)
fig.update_traces(texttemplate="%{text:.1f}%")
st.plotly_chart(fig, use_container_width=True)

#The final results
max_risk = risk.loc[risk["Stroke"].idxmax()]
st.subheader("Final Result")
st.info(f"Highest stroke risk: {max_risk['Gender']} ({max_risk['Stroke']*100:.1f}%)")