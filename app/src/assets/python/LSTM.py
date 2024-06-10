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
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import *
import keras
import logging


def predict(ticker, df):

    start_date = "2021-06-08"
    current_date = date.today()
    ## I grabbed the current date, will update as day changes
    end_date = "2024-06-08"
    # data = yf.download(ticker, start=start_date, end=end_date)
    # df = pd.DataFrame(data).reset_index()
    # df
    # create an array of close values, create a 90/10 split for training and test data
    df_close = df[["Close"]]
    df_close_data = df_close.values
 
    df_training_size = int(len(df_close_data) * .90)
    step = 70
    # scale the data between 0 and 1, sort the training and test data
    df_scaler = MinMaxScaler(feature_range = (0,1))
    df_scaled_data = df_scaler.fit_transform(df_close_data)
    df_training_data = df_scaled_data[0:df_training_size, :]
    df_testing_data = df_scaled_data[df_training_size-step: , :]
    # creating arrays of testing and training x and y data made up of arrays of the data used for each following
    # predictions, reshaping the data
    df_x_training = []
    df_y_training = []
    df_x_testing = []
#    df_y_testing = df_close_data[df_training_size:, :]
    for i in range(step, df_training_size):
        df_x_training.append(df_training_data[i-step:i, 0])
        df_y_training.append(df_training_data[i, 0])
    for i in range(step, len(df_testing_data)):
        df_x_testing.append(df_testing_data[i-step:i, 0])
    df_x_training = np.array(df_x_training)
    df_y_training = np.array(df_y_training)
    df_x_testing = np.array(df_x_testing)
    df_x_training = np.reshape(df_x_training, (df_x_training.shape[0], df_x_training.shape[1], 1))
    df_x_testing = np.reshape(df_x_testing, (df_x_testing.shape[0], df_x_testing.shape[1], 1))
    
    # creating, building, compiling, and training the LSTM model
    n = 128  #number of neurons used
    n2 = 64 #layering with another number of neurons
    df_model = Sequential()
    df_model.add(InputLayer(shape=(df_x_training.shape[1], 1)))
    df_model.add(LSTM(n, return_sequences=True))
    df_model.add(LSTM(n2, return_sequences=False))
    df_model.add(Dense(25))
    df_model.add(Dense(1))
    df_model.summary()
    keras.metrics.BinaryAccuracy(name="binary_accuracy", dtype=None, threshold=.5)
    df_model.compile(optimizer='adam', loss='mean_squared_error', metrics=[keras.metrics.BinaryAccuracy()])
    df_model.fit(df_x_training, df_y_training, batch_size=1, epochs=2)
    # getting predictions from the models
    df_testing_predictions = df_model.predict(df_x_testing)
    df_testing_predictions = df_scaler.inverse_transform(df_testing_predictions)
    df_training_predictions = df_model.predict(df_x_training)
    df_training_predictions = df_scaler.inverse_transform(df_training_predictions)
    # plotting the AAPL testing data and predictions
    df_training_closes = df_close[:df_training_size]
    df_actual_closes = df_close[df_training_size:].copy()
    df_actual_closes['predictions'] = df_testing_predictions



    fig = plt.figure(figsize=(16, 8))
    plt.plot(df_training_closes['Close'])
    plt.plot(df_actual_closes['Close'], color='green')
    plt.plot(df_actual_closes['predictions'], color='red')
    plt.title(f'Training, Actual, and Predicted Values of {ticker} Closes')
    plt.xlabel(f'Days from {start_date}')
    plt.ylabel('Closing Price ($)')
    plt.legend(('Training Data', 'Actual Close', 'Predicted Close'))
    # plt.show()
    # plotting the actual vs predicited closing prices
    df_actual_closes.plot(color=['green', 'red'])
    plt.title('Actual and Predicted Closing Prices')
    plt.xlabel(f'Day from {start_date}')
    plt.ylabel('Closing Price $')
    plt.legend(('Actual Close', 'Predicted Close'))
    # plt.show()
    return fig