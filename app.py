import pandas as pd
import requests
import streamlit as st
import time
from streamlit_option_menu import option_menu

# Custom CSS to center the dataframe
st.markdown(
    """
    <style>
    .dataframe-container {
        display: flex;
        width: 100%;
        justify-content: center;
               
    }
    .dataframe {
       justify-content: center;
        margin: auto;
        border-collapse: collapse;
        width: 100%;
    }
    .dataframe th, .dataframe td {
        border: 1px solid #ddd;
        padding: 8px;
    }
    .dataframe th {
        padding-top: 12px;
        padding-bottom: 12px;
        text-align: left;
        background-color: #f2f2f2;
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# sidebar menu
sidebar_Menu = 1
def streamlit_menu(sidebar_menu=1):
    if sidebar_menu == 1:
        # 1. as sidebar_menu
        with st.sidebar:
            selected = option_menu(
                menu_title="",
                options=["About Cake Afella", "General Cake Price", "Dounts","Cup Cakes", "Brownies"], 
                icons=["info-circle", "currency-dollar", "emoji-smile","cup-straw", "gift"], 
                menu_icon="cast", 
                default_index=0, 
            )
        return selected
selected = streamlit_menu(sidebar_menu=sidebar_Menu)
# Home Page
if selected == "About Cake Afella":
    st.image('Headerbanner.jpg')
    st.write("""
**At CakeAfella,** Our Exclusive assortment of permium and contemporay quality cakes is in high demand.

among clients who seek a cake that serves as an expression of their unique style.

**We are devoted** to staying ahead of the curve by embracing the latest trends and employing innovative 
             
techniques in the creation of our premium cakes. Our primary focus on style ensures that your cake 
             
designs remains timeless,leaving you with cherished memories that never lose their allure.""")
# General Cake Price details page
if selected == "General Cake Price":
        st.image('CakePrice.jpg')
             
#Dounts price details page
if selected == "Dounts":
        st.image('Donuts_Price.jpg')

#Cup Cakes price details page    
if selected == "Cup Cakes":
        st.image('CupCakes_Price.jpg')

#Brownies price details page
if selected == "Brownies":
        st.image('Brownies_Price.jpg')