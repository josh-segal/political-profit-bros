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
from datetime import datetime as dt
import uuid
from datetime import datetime, timedelta, date
import yfinance as yf
from sklearn.model_selection import train_test_split
from assets.python.phase3_python_functions import line_of_best_fit, linreg_predict
from dateutil.relativedelta import *
import plotly.graph_objects as go


logger = logging.getLogger()

SideBarLinks()


name_input = st.text_input('Enter Stock', 'BRP')

if name_input:
    st.write("You Chose:", name_input)
    """
    current_date = date.today()
    current_date_str = current_date.strftime('%Y-%m-%d')

    begin_date = current_date - relativedelta(months=+12)
    begin_date_str = begin_date.strftime('%Y-%m-%d')

    stock = yf.download([f'{name_input}'], start=begin_date_str, end=current_date_str).reset_index()
    # Convert dates to ordinal numbers
    stock['Date_ordinal'] = stock['Date'].apply(lambda date: date.toordinal())

    # Calculate the linear regression slope and intercep
    X = np.array(stock['Date_ordinal'])
    Y = np.array(stock['Adj Close'])
    equation = line_of_best_fit(X, Y)
    predict = linreg_predict(X, Y, equation)

    stock['Adj_Close_Pred'] = predict['ypreds']

    """


    """
    logger.info(f'encoded_name: {name_input}')
    stock_data, response = requests.get(f'http://api:4000/s/stocks/{name_input}') 
    logger.info(f'stock_data: {stock_data}')
    logger.info(f'response: {response}')

    

    # Plot the stock Adj Close values along with the calculated linear regression
    fig = go.Figure(data=[
        go.Candlestick(x=stock_data['Date'],
                    open=stock_data['Open'], high=stock_data['High'],
                    low=stock_data['Low'], close=stock_data['Close'])
    ])
    fig.add_trace(go.Scatter(x=stock_data['Date_ordinal'], y=response['y_preds'], mode='lines', line_color='red', name='Adj Close Prediction'))
    fig.update_layout(
        title=f'{name_input} Stock Price Over time',
        yaxis_title=f'{name_input} Stock',
        annotations=[
            dict(
                x=0.97, y=0.95, xref='paper', yref='paper',
                showarrow=False, xanchor='right', yanchor='top', 
                text=response['equation']
            )
        ]
    )

    st.plotly_chart(fig)
    """







"""
# Call the SideBarLinks from the nav module in the modules directory
SideBarLinks()
logger.info('01_Stock_Search page')
search_query = st.text_input('Search for a stock...')

if search_query:
    results = requests.get(f'http://api:4000/s/{search_query}').json()
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
    st.write("Trending Stocks:")

    # SQL query to grab 5 most searched stocks ... eventually
    results = requests.get(f'http://api:4000/s/stocks').json()
    for stock in results:
            if st.button(stock['company'],
                        type='primary',
                        use_container_width=True):
                st.session_state.payload = stock
                st.switch_page('pages/08_Stock_Detail.py')
"""