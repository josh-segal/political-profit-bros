import pandas as pd
import streamlit as st
from streamlit_extras.app_logo import add_logo
import world_bank_data as wb
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
from modules.nav import SideBarLinks
import requests

# Call the SideBarLinks from the nav module in the modules directory
SideBarLinks()

# set the header of the page
st.header('Portfolio')

# You can access the session state to make a more customized/personalized app experience
st.write(f"### Hi, {st.session_state['first_name']}. Here are the stocks you own.")

stock_pol = st.toggle("Politician / Stock Portfolio", value=True)

if stock_pol:
    results = requests.get(f'http://api:4000/i/stock_portfolio/{1}').json()
    if results:
        for stock in results:
                    if st.button(stock['company'],
                                type='primary',
                                use_container_width=True):
                        st.session_state.payload = stock
                        st.switch_page('pages/08_Stock_Detail.py')         
    else:
        st.write('no stocks found... check spelling')
else:
    results = requests.get(f'http://api:4000/po/politician_portfolio/{1}').json()
    if results:
        for politician in results:
                    if st.button(politician['name'],
                                type='primary',
                                use_container_width=True):
                        st.session_state.payload = politician
                        st.switch_page('pages/09_Politician_Detail.py')         
    else:
        st.write('no politician found... check spelling')
