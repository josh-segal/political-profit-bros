import streamlit as st
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

st.write("# About this App")

st.markdown (
    """
    Introducing Political Profit Bros, a cutting-edge political stock trading app designed to empower investors, campaign managers, and journalists with actionable insights. 
    Political Profit Bros harnesses the power of machine learning models to provide predictive analysis of stock prices influenced by politicians' trading activities and legislative developments. 
    By seamlessly integrating real-time data on political actions and market trends, Political Profit Bros offers a unique platform where users can make informed investment decisions, strategize campaign finances, and craft data-driven journalistic narratives. 
    Join Political Profit Bros today and stay ahead in the dynamic intersection of politics and finance.
    
    """
        )
