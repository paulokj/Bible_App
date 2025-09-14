# Core Pkgs
import streamlit as st
import streamlit.components.v1 as stc

# EDA pkgs
import pandas as pd
import neattext.functions as nfx

# Data Viz Pkgs
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import altair as alt

# Utils
from utils.home_app import home_page
from utils.multiverse_app import multiverse_page
from utils.about_app import about_page



def main():
    st.title("Addai Family Bible App")

    menu = ["Home", "MultiVerse", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        home_page()
        

    elif choice == "MultiVerse":
        multiverse_page()
        

    else:
        about_page()


if __name__=="__main__":
    main()