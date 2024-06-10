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


# Function to get stock data for a given ticker and date range
def get_stock_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    df = pd.DataFrame(data).reset_index()
    return df

# Function to preprocess the data for training and testing
def preprocess_data(df, step=70):
    # Rounding off the necessary columns
    columns_to_round = ['Open', "High", "Low", "Close", "Adj Close"]
    df[columns_to_round] = np.round(df[columns_to_round], 4)
    
    # Extracting the 'Close' prices
    df_close = df[["Close"]]
    df_close_data = df_close.values
    df_size = len(df_close_data)
    df_training_size = int(len(df_close_data) * .90)
    
    # Scaling the data between 0 and 1
    df_scaler = MinMaxScaler(feature_range=(0, 1))
    df_scaled_data = df_scaler.fit_transform(df_close_data)

    # Splitting the data into training and testing sets
    df_training_data = df_scaled_data[0:df_training_size, :]
    df_testing_data = df_scaled_data[df_training_size-step:, :]
    
    # Creating training and testing datasets
    df_x_training = []
    df_y_training = []
    df_x_testing = []
    df_y_testing = df_close_data[df_training_size:, :]

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
    
    return df_x_training, df_y_training, df_x_testing, df_y_testing, df_scaler, df_close, df_training_size

# Function to create and compile the LSTM model
def create_lstm_model(input_shape, n=128, n2=64):
    model = Sequential()
    model.add(InputLayer(input_shape=input_shape))
    model.add(LSTM(n, return_sequences=True))
    model.add(LSTM(n2, return_sequences=False))
    model.add(Dense(25))
    model.add(Dense(1))

    model.compile(optimizer='adam', loss='mean_squared_error', metrics=[keras.metrics.BinaryAccuracy()])
    return model

# Function to train the LSTM model
def train_model(model, df_x_training, df_y_training, epochs=1, batch_size=1):
    model.fit(df_x_training, df_y_training, batch_size=batch_size, epochs=epochs)
    return model

# Function to make predictions using the trained model
def make_predictions(model, df_x_training, df_x_testing, df_scaler):
    df_training_predictions = model.predict(df_x_training)
    df_training_predictions = df_scaler.inverse_transform(df_training_predictions)

    df_testing_predictions = model.predict(df_x_testing)
    df_testing_predictions = df_scaler.inverse_transform(df_testing_predictions)
    
    return df_training_predictions, df_testing_predictions

# Function to plot the actual and predicted values
def plot_predictions(df_close, df_training_size, df_training_predictions, df_testing_predictions, start_date):
    df_training_closes = df_close[:df_training_size]
    df_actual_closes = df_close[df_training_size:].copy()
    df_actual_closes['predictions'] = df_testing_predictions
    
    plt.figure(figsize=(16, 8))
    plt.plot(df_training_closes['Close'])
    plt.plot(df_actual_closes['Close'], color='green')
    plt.plot(df_actual_closes['predictions'], color='red')
    plt.title(f'Training, Actual, and Predicted Values of {ticker[0]} Closes')
    plt.xlabel(f'Days from {start_date}')
    plt.ylabel('Closing Price ($)')
    plt.legend(('Training Data', 'Actual Close', 'Predicted Close'))
    plt.show()

# Example usage:
ticker = ["TSLA"]
start_date = "2021-05-28"
end_date = date.today().strftime("%Y-%m-%d")

# Step 1: Get stock data
df = get_stock_data(ticker, start_date, end_date)

# Step 2: Preprocess the data
df_x_training, df_y_training, df_x_testing, df_y_testing, df_scaler, df_close, df_training_size = preprocess_data(df)

# Step 3: Create the LSTM model
input_shape = (df_x_training.shape[1], 1)
model = create_lstm_model(input_shape)

# Step 4: Train the LSTM model
model = train_model(model, df_x_training, df_y_training, epochs=1, batch_size=1)

# Step 5: Make predictions
df_training_predictions, df_testing_predictions = make_predictions(model, df_x_training, df_x_testing, df_scaler)

# Step 6: Plot the predictions
plot_predictions(df_close, df_training_size, df_training_predictions, df_testing_predictions, start_date)
