import pandas as pd
import streamlit as st
from streamlit_extras.app_logo import add_logo
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
from modules.nav import SideBarLinks
import requests
import logging
logger = logging.getLogger()
from datetime import datetime as dt
import uuid


# Call the SideBarLinks from the nav module in the modules directory
SideBarLinks()
logger.info('01_Stock_Search page')

stock = requests.get(f'http://api:4000/s/stocks_dropdown').json()

stocks = []

for s in stock:
     stocks.append(s['item'])

dropdown_list = pd.DataFrame(stock).values.astype(str)

search_query = st.selectbox('Search for a stock...', stocks, index=None)

# search_query = st.text_input('Search for a stock...')

if search_query:
    search_query = (search_query.split(" ")[0])
    results = requests.get(f'http://api:4000/s/{search_query}').json()
    if results:
        for stock in results:
            if st.button(stock['company'],
                        type='primary',
                        use_container_width=True,
                        key=f"{stock['ticker']}_name"):
                st.session_state.payload = stock
                st.switch_page('pages/08_Stock_Detail.py')
    else:
        st.write('no stocks found... check spelling')
         
    
else:
    col1, col2 = st.columns(2)
    with col1:
        st.write("Trending Stocks by PoliticalInterest Users:")

        # SQL query to grab 5 most searched stocks ... eventually
        results = requests.get(f'http://api:4000/s/stocks').json()
        for stock in results:
                if st.button('🔥 ' + stock['company'],
                            type='primary',
                            use_container_width=True,
                            key=f"{stock['ticker']}_trending"):
                    st.session_state.payload = stock
                    st.switch_page('pages/08_Stock_Detail.py')
    
    with col2:
        st.write("Stocks by Volume: ")
        results = requests.get(f'http://api:4000/s/stocks_volume').json()
        for stock in results:
            if st.button(stock['company'],
                            type='primary',
                            use_container_width=True,
                            key=f"{stock['ticker']}_volume"):
                st.session_state.payload = stock
                st.switch_page('pages/08_Stock_Detail.py')