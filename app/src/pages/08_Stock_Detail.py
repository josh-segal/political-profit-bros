import pandas as pd
import streamlit as st
from streamlit_extras.app_logo import add_logo
import numpy as np
from modules.nav import SideBarLinks
import requests
import logging
logger = logging.getLogger()
from datetime import datetime

SideBarLinks()

st.write('Stock Detail Page')
stock = st.session_state.payload
st.write(stock['company'])

ticker = stock['ticker']
def convert_date(date_string):
    # convert string to date object
    date_object = datetime.strptime(date_string, '%a, %d %b %Y %H:%M:%S %Z').date()
    return date_object
# dates = pd.date_range('2023-06-09', '2024-06-09')
data = requests.get(f'http://api:4000/s/stocks_closing_value/{ticker}').json()
logger.info(f'JSON: {data}')
df = pd.DataFrame(data)
df['Date'] = df['Date'].apply(lambda x: convert_date(x))
df = df.sort_values(by='Date', ascending=False)
st.line_chart(df, x='Date', y='Close')

if st.button('Track stock',
                        type='primary',
                        use_container_width=True):
    
    payload = {
            'investor_id': 1, # TODO: figure out how to do this with 3 users
            'stock_id': stock['ticker'],
            'date': datetime.now().isoformat(),
    }

    url = 'http://api:4000/s/track'
    search_history_url = 'http://api:4000/s/history'

    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            st.success('Stock successfully tracked!')
        else:
            st.error('Failed to track stock. Please try again.')
            logger.error(f"Failed to track stock: {response.status_code}, {response.text}")

        search_history_response = requests.post(search_history_url, json=payload)
        if search_history_response.status_code == 200:
            st.success('Search history successfully tracked!')
        else:
            st.error('Failed to track search history. Please try again.')
            logger.error(f"Failed to track search history: {search_history_response.status_code}, {search_history_response.text}")
    except requests.exceptions.RequestException as e:
        st.error('An error occurred while making requests. Please try again.')
        logger.error(f"RequestException: {e}")
