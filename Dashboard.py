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

#Set to 42 to be able to reproduce
np.random.seed(42)

#Number of "recorded" data
n = 500  

#My Synthetic database and its features
data = {
    "patient_id": range(1, n+1),
    "age": np.random.randint(18, 90, n),
    "gender": np.random.choice(["Male", "Female"], n),
    "hypertension": np.random.choice([0, 1], n, p=[0.8, 0.2]),
    "heart_disease": np.random.choice([0, 1], n, p=[0.9, 0.1]),
    "smoking_status": np.random.choice(["never", "formerly", "currently"], n, p=[0.5, 0.3, 0.2]),
    "bmi": np.round(np.random.normal(27, 5, n), 1),
    "avg_glucose_level": np.round(np.random.normal(100, 30, n), 1),
}

df = pd.DataFrame(data)

#Calculates the probability
prob_stroke = (
    0.01
    + 0.02 * df["hypertension"]
    + 0.03 * df["heart_disease"]
    + 0.02 * (df["smoking_status"] == "currently")
    + 0.01 * (df["age"] > 60)
)

df["stroke"] = np.random.binomial(1, np.clip(prob_stroke, 0, 1))

print(df.head())

#Showing the data
st.set_page_config(page_title="Stroke Risk by Gender", page_icon="🫀")
st.title("Stroke Risk by Gender")

#Grouping up the gender to calculate the stroke probability
risk_by_gender = df.groupby("gender")["stroke"].mean().reset_index()
risk_by_gender["stroke"] = risk_by_gender["stroke"] * 100  #Convert to percent

st.subheader("Percentage of patients who had a stroke by gender")
st.bar_chart(data=risk_by_gender.set_index("gender")["stroke"])

st.subheader("Data table")
st.dataframe(risk_by_gender)