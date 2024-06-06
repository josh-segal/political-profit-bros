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
from phase3_python_functions import line_of_best_fit, linreg_predict

# Read in the data
politician_data = pd.read_csv('/Users/asun/DS 3000/CS 4973/political-profit-bros/python/politician_dataset.csv', index_col=0)

# Sort values by Trade Value and only filter by Stocks
"""
politician_data.sort_values(by='Trade Value', ascending=False)[politician_data['Asset Type'] == 'Stock'].head(20)
"""
filtered_politician_data = politician_data[politician_data['Asset Type'] == 'Stock'].sort_values(by='Trade Value', ascending=False)
print(filtered_politician_data.head(20))


# Analyzed that brp stock was sold > 1M value
# Will analyze any significant stock price changes
brp = yf.download(['BRP'], start='2024-03-10', end='2024-05-01').reset_index()


# Calculate the linear regression slope and intercept
X = np.array(list(range(1, len(brp) + 1)))
Y = np.array(brp['Adj Close'])
equation = line_of_best_fit(X, Y)
predict = linreg_predict(X, Y, equation)

brp['Adj Close Pred'] = predict['ypreds']

# Plot the stock Adj Close values along with the calculated linear regression
fig = go.Figure(data=[go.Candlestick(x=brp['Date'],
                open=brp['Open'], high=brp['High'],
                low=brp['Low'], close=brp['Close'])
                      ])
fig.add_trace(go.Scatter(x=brp['Date'], y=brp['Adj Close Pred'], mode='lines', name='Adj Close Prediction'))
fig.update_layout(
    title='BRP Stock Price Over time [Clifford Franklin (R)]',
    yaxis_title='BRP Stock',
    shapes = [dict(
        x0='2024-03-21', x1='2024-03-21', y0=0, y1=1, xref='x', yref='paper',
        line_width=2)],
    annotations=[
        dict(
        x='2024-03-21', y=0.05, xref='x', yref='paper',
        showarrow=False, xanchor='left', text='When stock was sold'),
        dict(
            x=0.97, y=0.95, xref='paper', yref='paper',
            showarrow=False, xanchor='right', yanchor='top', 
            text=f'y = {equation[1]:.3f}x + {equation[0]:.3f}, MSE = {predict["mse"]:.3f}, R^2 = {predict["r2"]:.3f}')

        ]
    )
#fig.show()
print(brp)

def plot_linear_regression(stock_ticker, start_date='2024-03-10', end_date='2024-05-01'):

    stock_df = yf.download([stock_ticker], start=start_date, end=end_date).reset_index()
    # Calculate the linear regression slope and intercept
    X = np.array(list(range(1, len(stock_df) + 1)))
    Y = np.array(stock_df['Adj Close'])
    equation = line_of_best_fit(X, Y)
    predict = linreg_predict(X, Y, equation)
    stock_df['Adj Close Pred'] = predict['ypreds']


    # Plot the stock Adj Close values along with the calculated linear regression
    fig = go.Figure(data=[go.Candlestick(x=stock_df['Date'],
                    open=stock_df['Open'], high=stock_df['High'],
                    low=stock_df['Low'], close=stock_df['Close'])
                        ])
    fig.add_trace(go.Scatter(x=stock_df['Date'], y=stock_df['Adj Close Pred'], mode='lines', name='Adj Close Prediction'))
    fig.update_layout(
        title=f'{stock_ticker} Stock Price Over time',
        yaxis_title=f'{stock_ticker} Stock',
        shapes = [dict(
            ### Fix!!!!
            ###
            x0='2024-03-21', x1='2024-03-21', y0=0, y1=1, xref='x', yref='paper',
            line_width=2)],
        annotations=[
            dict(
            x='2024-03-21', y=0.05, xref='x', yref='paper',
            showarrow=False, xanchor='left', text='When stock was sold'),
            dict(
                x=0.97, y=0.95, xref='paper', yref='paper',
                showarrow=False, xanchor='right', yanchor='top', 
                text=f'y = {equation[1]:.3f}x + {equation[0]:.3f}, MSE = {predict["mse"]:.3f}, R^2 = {predict["r2"]:.3f}')

            ]
        )
    return fig
#plot_linear_regression('BRP')
    


def test_model(stock_df, predict_stock):
    # Checking Assumptions
    # Checking for linearity and homoscedasticity
    print('Checking for linearity and homoscedasticity...')
    plt.scatter(stock_df['Date'], stock_df['resids'])
    plt.xticks(rotation=45)
    plt.xlabel('Date')
    plt.ylabel('Adj Close Residuals')
    plt.title('Residual plot vs Date')
    plt.grid()
    plt.show()
    # Histogram of residuals
    print('Plotting Historgram ...')
    sns.histplot(predict_stock['resids'], kde=False, bins = 10)
    plt.xlabel("residuals")
    plt.title("histogram of residuals")
    plt.grid()
    plt.show()
    # Checking for No Autocorrelation (plotting by order)
    print('Checking for No Autocorrelation (plotting by order)...')
    plt.scatter(range(len(stock_df['Date'])), predict_stock['resids'], alpha=0.8)
    plt.xlabel("index")
    plt.ylabel("Adj Close residuals")
    plt.title("residual plot vs. order")
    plt.grid()
    plt.show()


def cross_validate(stock_df, test_size=0.3, random_state=3):
    # Test size 30%
    x_value = np.array(list(range(1, len(stock_df) + 1)))
    y_value = np.array(stock_df['Adj Close'])
    crossval = train_test_split(x_value,
                                y_value,
                                test_size=test_size,
                                random_state=random_state)

    Xtrain, Xtest, ytrain, ytest = crossval
    cross_equation = line_of_best_fit(Xtest, ytest)
    cross_predict = linreg_predict(Xtest, ytest, cross_equation)
    print(f'Mean Squared Error: {cross_predict["mse"]} \n'
      f'R^2 score: {cross_predict["r2"]}')

def main():
    #test_model(brp, predict)

    #cross_validate(brp)

    fig = plot_linear_regression('BRP')

    st.plotly_chart(fig)

    st.write('hello')

    




if __name__ == '__main__':
    main()




 







