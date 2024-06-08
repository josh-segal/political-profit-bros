import pandas as pd
import streamlit as st
from streamlit_extras.app_logo import add_logo
import world_bank_data as wb
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
from modules.nav import SideBarLinks
import requests
import logging
logger = logging.getLogger()
from datetime import datetime as dt


# Call the SideBarLinks from the nav module in the modules directory
SideBarLinks()
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