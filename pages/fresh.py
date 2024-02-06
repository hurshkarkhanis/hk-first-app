# example/st_app.py

import streamlit as st
from streamlit_gsheets import GSheetsConnection

url = "https://docs.google.com/spreadsheets/d/1vW1qzYSqPyWxZAyraNM83V8AzPotnOlfXT35ZbvfnfE/edit?usp=sharing"

conn = st.experimental_connection("gsheets", type=GSheetsConnection)

data = conn.read(spreadsheet=url, usecols=[0, 1])
st.dataframe(data)