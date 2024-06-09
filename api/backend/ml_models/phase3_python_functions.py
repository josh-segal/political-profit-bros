import numpy as np
import pandas as pd
from sklearn.metrics import r2_score
import yfinance as yf


def add_bias_column(X):
    """
    Args:
        X (array): can be either 1-d or 2-d
    
    Returns:
        Xnew (array): the same array, but 2-d with a column of 1's in the first spot
    """
    
    # If the array is 1-d
    if len(X.shape) == 1:
        Xnew = np.column_stack([np.ones(X.shape[0]), X])
    
    # If the array is 2-d
    elif len(X.shape) == 2:
        bias_col = np.ones((X.shape[0], 1))
        Xnew = np.hstack([bias_col, X])
        
    else:
        raise ValueError("Input array must be either 1-d or 2-d")

    return Xnew

def line_of_best_fit(X, Y): 
    """
    finds the line of best fit of two arrays using the (XtX)^-1Xty equation
    
    Args:
        x (array): either 1-d or 2-d
        y (array): 1-d
    
    Return:
        m (array): vector including intercept(first num) and slope(second num) for line of best fit
    
    """
    
    X_into_array = add_bias_column(X)
    XtXinv = np.linalg.inv(np.matmul(X_into_array.T, X_into_array))
    m = np.matmul(XtXinv, np.matmul(X_into_array.T, Y))
    
    return m

def linreg_predict(Xnew, ynew, m):
    """
    Predicts the linear regression and gives it a score on how well the variance is explained
    Args: 
        Xnew (array): either 1-d or 2-d, includes all p predictor features
        ynew (array): 1-d array, includes all correspondign response values to Xnew
        m (array): array that shows the intercept and the slope to be used for calculating ypreds
        
    Returns:
        dictionary (dict): four key-value pairs (ypreds, resids, mse, r2)
    
    """
    Xnew = add_bias_column(Xnew)
    ypreds = np.matmul(Xnew, m)
    resids = ynew - ypreds
    mse = (resids**2).sum()/resids.size
    r2 = r2_score(ynew, ypreds)
    
    dictionary = {'ypreds': ypreds,
                  'resids':resids,
                  'mse':mse,
                  'r2':r2,
                  'equation': f'y = {m[1]:.3f}x + {m[0]:.3f}, MSE = {mse:.3f}, R^2 = {r2:.3f}'
                 }
    return dictionary

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