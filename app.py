import streamlit as st
import pandas as pd
!pip install matplotlib 

import matplotlib.pyplot as plt
import seaborn as sns

st.title("Finance Data Viewer")

CSV_URL = "https://raw.githubusercontent.com/fakhitah3/DS2925/refs/heads/main/Finance_data.csv"
# Load the data
df = pd.read_csv(CSV_URL)

st.subheader("Data Preview")
st.write(df.head())

# Histogram of Age
fig, ax = plt.subplots(figsize=(8, 6))
sns.histplot(data=df, x='age', kde=True, ax=ax)
ax.set_title('Histogram of Age')
ax.set_xlabel('Age')
ax.set_ylabel('Frequency')

st.pyplot(fig)

