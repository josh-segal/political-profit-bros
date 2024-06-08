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
logger = logging.getLogger(__name__)
from datetime import datetime as dt
import uuid


# Call the SideBarLinks from the nav module in the modules directory
SideBarLinks()
logger.info('01_Stock_Search page')

import streamlit as st

option = st.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone"), index=None)

st.write("You selected:", option)

stock = requests.get(f'http://api:4000/s/dylan').json()
# logger.info(f'stock = {stock}')

stocks = []

for element in stock:
    # logger.info(f'element = {element}')
    # logger.info(f'   item = {element["item"]}')
    stocks.append(element["item"])

# logger.info(f'stocks = {stocks}')

#search_query = st.text_input('Search for a stock...')
dropdown_list = pd.DataFrame(stock).values.astype(str)#.reshape(-1,)

#define function
#map_strings = lambda x: x.replace("['",'').replace("']",'')

#dropdown_list2 = [map_strings(y) for y in dropdown_list]

# Stock_Name = list(dropdown_list.columns)[0]
# dropdown_list[Stock_Name] = dropdown_list[Stock_Name].split()[0][1:]
# logger.info("eroifuerlifuhrelfuherlifu",dropdown_list)
# for i in dropdown_list:
#     i.split()[0][2:]


#string_data = sample_df.values.astype(str).reshape(-1,)

# search = st.selectbox('Search for a stock...', dropdown_list, index=None)
search = st.selectbox('Search for a stock...', stocks, index=None)

# logger.info(f'search = {(search.split(" "))[0]}')

if search != None:
    # search_query = search[0].replace("['", '').split(" ")[0]
    search_query = (search.split(" "))[0]
    # if st.button("Search"):
    #     st.session_state.payload = search
    #     st.switch_page('pages/08_Stock_Detail.py')
    if search_query:
        results = requests.get(f'http://api:4000/s/stock_get/{search_query}').json()
        if results:
            for stock in results:
                if st.button(f'See Details for {stock["company"]}',
                            type='primary',
                            use_container_width=True):
                    st.session_state.payload = stock
                    st.switch_page('pages/08_Stock_Detail.py')
        else:
            st.write('no stocks found... check spelling')
    
else:
    st.write("Trending Stocks:")

    # SQL query to grab 5 most searched stocks ... eventually
    results = requests.get(f'http://api:4000/s/stocks').json()
    for stock in results:
            if st.button(stock['company'],
                        type='primary',
                        use_container_width=True):
                st.session_state.payload = stock
                st.switch_page('pages/08_Stock_Detail.py')