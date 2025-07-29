# 📊 Trading Strategy Explorer Dashboard

This is an interactive dashboard built using Python and Streamlit that allows users to upload CSV files with stock trading data and visualize trends such as **Close Price Over Time**.

## 🚀 Features

- Drag and drop CSV upload (up to 200MB)
- Interactive preview of uploaded trading data
- Line chart visualization of Close Prices over time
- Uses default sample data if no file is uploaded

## 📂 Sample Input Format

The CSV file should contain the following columns:

- `timestamp`
- `open`
- `high`
- `low`
- `close`
- `volume`

## 📷 Screenshots

### 1. Upload & Data Preview

<img width="1804" height="780" alt="Screenshot 2025-07-29 233102" src="https://github.com/user-attachments/assets/695a59c4-ba55-4efb-9faf-acad406b82f6" />



### 2. Close Price Graph

<img width="1732" height="656" alt="Screenshot 2025-07-29 233055" src="https://github.com/user-attachments/assets/30ccc5d9-a5e3-4221-b1b0-43cc2646b48f" />

## 📦 How to Run

```bash
pip install streamlit pandas matplotlib
streamlit run app.py
