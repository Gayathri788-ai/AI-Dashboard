@@ -0,0 +1,66 @@
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="AI Dashboard", layout="wide")

st.title("🎬 Netflix AI Dashboard")

df = pd.read_csv("data/netflix.csv")


st.header("Dataset Overview")
st.write("Rows and Columns:", df.shape)
st.dataframe(df)


st.header("Data Cleaning")
df = df.drop_duplicates()
df = df.dropna()

st.success("Duplicates and Missing Values Removed")


st.header("Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Titles", len(df))
col2.metric("Movies", len(df[df["type"] == "Movie"]))
col3.metric("TV Shows", len(df[df["type"] == "TV Show"]))


st.sidebar.header("Filters")

selected_type = st.sidebar.selectbox(
    "Select Type",
    df["type"].unique()
)

filtered_df = df[df["type"] == selected_type]


st.subheader("Titles by Genre")
fig1 = px.histogram(filtered_df, x="genre")
st.plotly_chart(fig1)


st.subheader("Titles by Country")
fig2 = px.histogram(filtered_df, x="country")
st.plotly_chart(fig2)


st.subheader("Release Year Distribution")
fig3 = px.histogram(filtered_df, x="release_year")
st.plotly_chart(fig3)


st.subheader("Rating Distribution")
fig4 = px.pie(filtered_df, names="rating")
st.plotly_chart(fig4)


st.subheader("Genre Distribution")
fig5 = px.pie(filtered_df, names="genre")
st.plotly_chart(fig5)
