import pandas as pd
import streamlit as st
from streamlit_extras.app_logo import add_logo
import numpy as np
from modules.nav import SideBarLinks
import requests
import logging
logger = logging.getLogger()
from datetime import datetime as dt

SideBarLinks()

st.write('Stock Detail Page')
stock = st.session_state.payload
st.write(stock['company'])

dates = pd.date_range('2023-01-01', periods=100)
data = np.random.randn(100).cumsum()
df = pd.DataFrame(data, index=dates, columns=['Value'])
st.line_chart(df)

if st.button('Track stock',
                        type='primary',
                        use_container_width=True):
    
    payload = {
            'investor_id': 1, # TODO: figure out how to do this with 3 users
            'stock_id': stock['id'],
            'date': dt.now().isoformat(),
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
