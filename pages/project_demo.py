import yfinance as yf
import streamlit as st
import pandas as pd
import time
import numpy as np





msft = yf.Ticker("MSFT")




# get all stock info

month_price = msft.history(period="1mo")


st.dataframe(month_price)
st.title("hk")

activated = st.toggle("Background App Refresh")


st.write("hk")
st.divider()
st.write("sk")

oscar = pd.read_csv("/workspaces/hk-first-app/pages/oscar.csv")

st.bar_chart(oscar.set_index("Year")["Age"])

st.data_editor(oscar)

st.metric("points", 30, 2)

msft.insider_transactions