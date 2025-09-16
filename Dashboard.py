import streamlit as st

st.set_page_config(
    page_title=("Assignment Dashboard"),
    page_icon=("📊"),
)

# Sidebar configuration
st.sidebar.image("./assets/project-logo.jpg",)
#Widget 1: Adding a button that would take the user to the 2nd page "About"
st.sidebar.button("About")

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

#Synthetic data set
np.random.seed(42)
df = pd.DataFrame({
    "PatientID": range(1, 501),
    "Gender": np.random.choice(["Male","Female"], 500),
    "Stroke": np.random.binomial(1, 0.1, 500)
})

#Calculating the risk of stroke between gender
risk = df.groupby("Gender")["Stroke"].mean().reset_index()
risk["stroke_percent"] = (risk["Stroke"]*100).round(1)

df_display = df.copy()
df_display["Stroke"] = df_display["Stroke"].map({0: "No", 1: "Yes"})

#The full dataset
st.subheader("Full Synthetic Dataset")
st.dataframe(df_display, height=300)

# Widget 2: Gives the user the ability to scroll through both or one gender at a time
gender = st.radio(
    "Choose Gender",
    ["Both", "Male", "Female"],
    index=None,
)

st.write("You selected:", gender)

#The results in a chart
colors = {"Male":"blue","Female":"red"}
fig = px.bar(
    risk,
    x="Gender",
    y="Stroke",
    color="Gender",
    color_discrete_map=colors,
    text=risk["stroke_percent"]
)
fig.update_layout(
    yaxis_title="Stroke Risk (%)",
    yaxis_tickformat=".1%",
    showlegend=False
)
fig.update_traces(texttemplate="%{text:.1f}%")
st.plotly_chart(fig, use_container_width=True)

#The final result
max_risk = risk.loc[risk["Stroke"].idxmax()]
st.subheader("Final Result")
st.info(f"Highest stroke risk: {max_risk['Gender']} ({max_risk['stroke_percent']:.1f}%)")