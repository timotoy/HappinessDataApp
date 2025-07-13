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

def get_x():
    for selectable in selectables:
        if selectable == horizontal:
            chosen_horizontal = selectable.replace(" ", "_").lower()
    return chosen_horizontal

def get_y():
    for selectable in selectables:
        if selectable == vertical:
            chosen_vertical = selectable.replace(" ", "_").lower()
    return chosen_vertical

x = get_x()
y = get_y()

fig = px.scatter(
    df,
    x=x,
    y=y,
    hover_name="country",
    title=f"{vertical} vs {horizontal}",
    labels={x: horizontal, y: vertical}
)

st.plotly_chart(fig)