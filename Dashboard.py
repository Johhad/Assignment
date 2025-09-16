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

#Synthetic dataset
np.random.seed(42)
df = pd.DataFrame({
    "gender": np.random.choice(["Male","Female"], 500),
    "stroke": np.random.binomial(1, 0.1, 500)
})

#Calculatin stroke risk between genders
risk = df.groupby("gender")["stroke"].mean().reset_index()  # 0-1 proportion

#Data table
st.subheader("Stroke Risk Data")
st.dataframe(risk.assign(stroke_percent=(risk["stroke"]*100).round(1)))

#The chart
colors = {"Male":"blue","Female":"red"}
fig = px.bar(
    risk,
    x="gender",
    y="stroke",
    color="gender",
    color_discrete_map=colors,
    text=(risk["stroke"]*100).round(1)
)
fig.update_layout(
    yaxis_title="Stroke Risk (%)",
    yaxis_tickformat="%",  # axis shows percentages
    showlegend=False
)
fig.update_traces(texttemplate="%{text:.1f}%")
st.plotly_chart(fig, use_container_width=True)

#Final Result
max_risk = risk.loc[risk["stroke"].idxmax()]
st.subheader("Final Result")
st.info(f"Highest stroke risk: {max_risk['gender']} ({max_risk['stroke']*100:.1f}%)")