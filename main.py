import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="CompareCountries")

st.header("Compare Countries")
st.text("Tak poprvýkrát som v kúte")

df = pd.read_csv("happy.csv")

selectables = ["Happiness", "GDP", "Social support", "Life expectancy",
                                        "Freedom to make life choices", "Corruption", "Generosity"]

horizontal = st.selectbox("Select horizontal axis", selectables)
vertical = st.selectbox("Select vertical axis", selectables)

x = horizontal.replace(" ", "_").lower()
y = vertical.replace(" ", "_").lower()

fig = px.scatter(
    df,
    x=x,
    y=y,
    hover_name="country",
    title=f"{vertical} vs {horizontal}",
    labels={x: horizontal, y: vertical}
)

st.plotly_chart(fig)