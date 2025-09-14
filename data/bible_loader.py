# Core pkg
import streamlit as st

# EDA
import pandas as pd

@st.cache_resource
def load_bible(data):
    df = pd.read_csv(data)
    return df