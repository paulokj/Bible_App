# Core pkg
import streamlit as st

# EDA
import pandas as pd

# Bible loader
from data.bible_loader import load_bible

def about_page():
    st.subheader("About Page")
    # df = load_bible('data/KJV_Bible.csv')
    # st.dataframe(df)