import streamlit as st
import pandas as pd
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


# Gender counts
gender_counts = df['gender'].value_counts()

# Create figure
fig, ax = plt.subplots(figsize=(6, 6))
ax.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90)
ax.set_title('Distribution of Gender')
ax.axis('equal')  # Equal aspect ratio ensures a circle

# Show in Streamlit
st.pyplot(fig)


