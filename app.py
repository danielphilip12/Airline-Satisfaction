import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Airline Satisfaction Explorer", page_icon="🛩️")

page = st.sidebar.selectbox(
    "Select a Page", ["Home", "Data Overview", "Exploratory Data Analysis"]
)

df = pd.read_csv("./data/cleaned_airline.csv")

if page == "Home":
    st.title("Airline Dataset Explorer")

elif page == "Exploratory Data Analysis":
    st.title("Exploratory Data Analysis (EDA)")

    st.subheader("Select the type of visualization you'd like to explore:")
    eda_type = st.multiselect(
        "Visualization Options",
        ["Histograms", "Box Plots", "Scatterplots", "Count Plots"],
    )

    obj_cols = df.select_dtypes(include="object").columns.tolist()
    num_cols = df.select_dtypes(include="number").columns.tolist()

    if "Histograms" in eda_type:
        h_selected_col = st.selectbox(
            "Select a numerical column for the histogram", num_cols
        )
        group_by_col = st.selectbox("Group by", obj_cols, index=None)
        if h_selected_col and group_by_col:
            st.plotly_chart(
                px.histogram(
                    df, x=h_selected_col, color=group_by_col, barmode="overlay"
                )
            )
        elif h_selected_col:
            st.plotly_chart(px.histogram(df, x=h_selected_col))

    if "Box Plots" in eda_type:
        b_selected_col = st.selectbox(
            "Select a numerical column for the histogram", num_cols
        )
        group_by_col = st.selectbox("Group by", obj_cols, index=None)
        if b_selected_col and group_by_col:
            st.plotly_chart(
                px.box(
                    df, x=b_selected_col, color=group_by_col
                )
            )
        elif b_selected_col:
            st.plotly_chart(px.box(df, x=b_selected_col))