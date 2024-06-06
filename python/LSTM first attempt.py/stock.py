import json 
import pandas as pd 
import requests 
import yfinance as yf 
import os
import plotly.express as px 
from datetime import datetime
import plotly.graph_objects as go
import numpy as np
import matplotlib.pyplot as plt
from datetime import date
import tensorflow as tf

stock1 = "AAPL"

ticker = [stock1] 

start_date = "2021-05-28"
current_date = date.today()
## I grabbed the current date, will update as day changes 
end_date = current_date.strftime("%Y-%m-%d")
data = yf.download(ticker, start=start_date, end=end_date)
df = pd.DataFrame(data).reset_index()

columns_to_round = ['Open', "High", "Low", "Close", "Adj Close"]
df[columns_to_round] = np.round(df[columns_to_round], 4)

from sklearn.preprocessing import MinMaxScaler,  RobustScaler, MaxAbsScaler, StandardScaler, Normalizer

scalers = {
    'MinMax':       MinMaxScaler(feature_range=(0, 1)),
    'RobustScaler': RobustScaler(quantile_range=(25.0, 75.0)),
    'MaxAbs':       MaxAbsScaler(),
    'Standard':     StandardScaler(),
    'Normalizer':   Normalizer()
}

def preprocess(data, scaling_method):
    # Create a copy of the DataFrame to avoid modifying the original
    data_copy = data.copy()
    del data_copy["Date"], data_copy["Adj Close"]
    if scaling_method is not None:
        scaler = scalers[scaling_method]
        data_copy = scaler.fit_transform(data_copy)
    return data_copy
    
def read_data(preprocessing=True, scaling_method='MinMax'):
    train_data = df
    test_data = df.copy()

    if preprocessing:
        train_data = preprocess(train_data, scaling_method)
        test_data = preprocess(test_data, scaling_method)
    return train_data, test_data

# Constructs dataframes for both train and test data.
def construct_time_frames(data, frame_size=64):
    num_of_samples = data.shape[0]
    x_train = [data[i-frame_size: i] for i in range(frame_size, num_of_samples)]
    y_train = [data[i, 0: 1] for i in range(frame_size, num_of_samples)]

    return np.array(x_train), np.array(y_train)

# Visualising the prediction & actual stock open value.
def plot_prediction(y_test, y_predicted, test_label, prediction_label):
    plt.plot(y_test, color='red', label=test_label)
    plt.plot(y_predicted, color='blue', label=prediction_label)
    plt.title('Tesla Stock Price Prediction')
    plt.xlabel('Time')
    plt.ylabel('Open Stock Price')
    plt.legend()
    plt.show()
    
    
