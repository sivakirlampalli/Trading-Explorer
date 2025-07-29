
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Trading Strategy Explorer Dashboard", layout="wide")

st.title("📈 Trading Strategy Explorer Dashboard")
st.markdown("Upload your CSV file to begin")

uploaded_file = st.file_uploader("Drag and drop file here", type=["csv"])

def load_data(file):
    data = pd.read_csv(file)
    for col in data.columns:
        if 'time' in col.lower() or 'date' in col.lower():
            data[col] = pd.to_datetime(data[col])
            data.set_index(col, inplace=True)
            break
    return data

if uploaded_file is not None:
    data = load_data(uploaded_file)
else:
    st.info("Using default sample data.")
    data = load_data("data/EOS_BTC_sample.csv")

st.subheader("Preview of Data")
st.dataframe(data.head())

st.subheader("📊 Close Price")
fig, ax = plt.subplots(figsize=(12, 4))
ax.plot(data['close'], label='Close Price', color='blue')
ax.set_title('Close Price Over Time')
ax.set_ylabel('Price')
ax.legend()
st.pyplot(fig)
