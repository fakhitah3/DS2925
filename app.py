import streamlit as st
import pandas as pd

st.title("Finance Data Viewer")

CSV_URL = "https://raw.githubusercontent.com/fakhitah3/DS2925/refs/heads/main/Finance_data.csv"
# Load the data
df = pd.read_csv(CSV_URL)

st.subheader("Data Preview")
st.write(df.head())
