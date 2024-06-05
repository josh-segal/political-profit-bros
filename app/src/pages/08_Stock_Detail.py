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

volume = st.number_input("How many shares...", min_value=1, value=1, step=1)
buy_sell = st.selectbox(
    "Buy or Sell",
    ("Buy", "Sell"))

if st.button('Buy Stock',
                        type='primary',
                        use_container_width=True):
    buy_sell_value = 1 if buy_sell == "Buy" else 0

    payload = {
            'price': stock['curr_price'],
                    'buy': buy_sell_value,
                    'stock_id': stock['id'],
                    'investor_id': 1, #TODO: change to specific investor users
                    'volume': volume,
                    'date': dt.now().isoformat(),
    }

    url = 'http://api:4000/s/track'

    response = requests.post(url, json=payload)

    logger.info('respose', response)
    if response.status_code == 200:
        st.success('Stock successfully tracked!')
    else:
        st.error('Failed to track stock. Please try again.')

