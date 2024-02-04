import pandas as pd
import streamlit as st

def my_demo():
    df = pd.read_csv("/workspaces/hk-first-app/pages/oscar.csv")
    df = df.set_index("Index")
    

my_demo()




