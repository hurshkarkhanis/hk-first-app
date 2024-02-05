import pandas as pd
import streamlit as st

    
# Sample data
bball = {'game': [0, 1, 2, 3, 4],
        'pts': [23, 24, 29, 19, 21]}

# Create a DataFrame
df = pd.DataFrame(bball)

# Streamlit app
st.title('Line Chart App')

# Line chart
st.line_chart(df.set_index('game'))

# Display raw data
st.dataframe(df)

oscar = pd.read_csv("/workspaces/hk-first-app/pages/oscar.csv")

print(oscar)
st.title("Oscars Best Actor Age")
st.bar_chart(oscar.set_index('Year')["Net Worth"])
st.dataframe(oscar)








