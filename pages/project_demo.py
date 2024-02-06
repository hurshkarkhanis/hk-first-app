import yfinance as yf

import streamlit as st


import pandas as pd
import time
import numpy as np
import datetime









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

raw_data = {'date': [0, 1, 2, 3, 4],
        'price': [23, 24, 29, 19, 21]}

markets = pd.DataFrame(raw_data)

st.line_chart(markets.set_index('date'))

iterations = st.slider("Level of detail", 2, 20, 10, 1)
separation = st.slider("Separation", 0.7, 2.0, 0.1)



today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)
start_date = st.date_input('Start date', today)
end_date = st.date_input('End date', tomorrow)
if start_date < end_date:
    st.success('Start date: `%s`\n\nEnd date:`%s`' % (start_date, end_date))
else:
    st.error('Error: End date must fall after start date.')

