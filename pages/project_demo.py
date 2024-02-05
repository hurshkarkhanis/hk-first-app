import yfinance as yf
import streamlit as st
import pandas as pd




msft = yf.Ticker("MSFT")


# get all stock info

month_price = msft.history(period="1mo")


st.dataframe(month_price)

