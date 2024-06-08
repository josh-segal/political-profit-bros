import pandas as pd
import streamlit as st
#from streamlit_extras.app_logo import add_logo
#import world_bank_data as wb
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
from modules.nav import SideBarLinks
import requests
import logging
from datetime import datetime as dt
import uuid
import urllib.parse


logger = logging.getLogger()


# Call the SideBarLinks from the nav module in the modules directory
SideBarLinks()

st.header("Type the Politician's first and last name")

name_input = st.text_input('Politician Name', "Doris Matsui")

if name_input:
    try:
        # URL encode the name_input to handle spaces and special characters
        encoded_name = urllib.parse.quote(name_input)
        logger.info(f'encoded_name: {encoded_name}')
        response = requests.get(f'http://api:4000/po/politicians/{encoded_name}') 
        logger.info(f'byebyebyebye{response}')
        results = response.json()
        st.dataframe(results, column_order=["Name", "Politician_id", "Party", "Chamber", "State", "Asset_Type", \
         "Issuer", "Ticker", "Issuer_Country", "Type", "txId", "Date_Traded", "Date_Published", "Trade_Size",\
             "Trade_Price", "Trade_Value"])
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {e}")





"""

search_query = st.text_input('Search for a politician...')



if search_query:
    results = requests.get(f'http://api:4000/po/{search_query}').json()
    if results:
        for politician in results:
            if st.button(politician['name'],
                        type='primary',
                        use_container_width=True):
                st.session_state.payload = politician
                st.switch_page('pages/09_Politician_Detail.py')
    else:
        st.write('no politicians found... check spelling')
        
    
else:
    st.write("Trending Politicians:")

    # SQL query to grab 5 most searched politicians ... eventually
    results = requests.get(f'http://api:4000/po/politicians').json()
    for politician in results:
            if st.button(politician['name'],
                        type='primary',
                        use_container_width=True):
                st.session_state.payload = politician
                st.switch_page('pages/09_Politician_Detail.py')
"""
