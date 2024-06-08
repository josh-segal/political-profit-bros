# Import necessary Libraries
import numpy as np
import pandas as pd
import seaborn as sns
import yfinance as yf
import plotly.graph_objects as go
import matplotlib.pyplot as plt 
import streamlit as st
import plotly.express as px
from datetime import datetime, timedelta
from dateutil.relativedelta import *
from sklearn.model_selection import train_test_split
from assets.python.phase3_python_functions import line_of_best_fit, linreg_predict
from modules.nav import SideBarLinks

SideBarLinks()
# st.write('This is a static image of our model inferencing in real-time, internet is too slow to build app again with needed dependencies to run model')
# st.image('assets/lin_reg_stock_price.png')


st.write('this shows up')

name_input = st.text_input('Enter Stock', 'BRP')
date_input = st.date_input('Enter Date Politician Bought/Sold', value=None)

if name_input and date_input:

    date_str = date_input.strftime('%Y-%m-%d')

    begin_date = date_input - timedelta(days=10)
    begin_date_str = begin_date.strftime('%Y-%m-%d')

    end_date = date_input + relativedelta(months=+1)
    end_date_str = end_date.strftime('%Y-%m-%d')


    # Analyzed that brp stock was sold > 1M value
    # Will analyze any significant stock price changes
    stock = yf.download([f'{name_input}'], start=begin_date_str, end=end_date_str).reset_index()


    # Calculate the linear regression slope and intercept
    X = np.array(list(range(1, len(stock) + 1)))
    Y = np.array(stock['Adj Close'])
    equation = line_of_best_fit(X, Y)
    predict = linreg_predict(X, Y, equation)

    stock['Adj_Close_Pred'] = predict['ypreds']

    # Plot the stock Adj Close values along with the calculated linear regression
    fig = go.Figure(data=[
        go.Candlestick(x=stock['Date'],
                    open=stock['Open'], high=stock['High'],
                    low=stock['Low'], close=stock['Close'])
    ])
    fig.add_trace(go.Scatter(x=stock['Date'], y=stock['Adj_Close_Pred'], mode='lines', line_color='red', name='Adj Close Prediction'))
    fig.update_layout(
        title=f'{name_input} Stock Price Over time',
        yaxis_title=f'{name_input} Stock',
        shapes=[
            dict(
                x0=date_str, x1=date_str, y0=0, y1=1, xref='x', yref='paper',
                line_width=2, line_color='blue'
            )
        ],
        annotations=[
            dict(
                x=date_str, y=0.05, xref='x', yref='paper',
                showarrow=False, xanchor='left', text='When stock was sold'
            ),
            dict(
                x=0.97, y=0.95, xref='paper', yref='paper',
                showarrow=False, xanchor='right', yanchor='top', 
                text=f'y = {equation[1]:.3f}x + {equation[0]:.3f}, MSE = {predict["mse"]:.3f}, R^2 = {predict["r2"]:.3f}'
            )
        ]
    )

    st.plotly_chart(fig)