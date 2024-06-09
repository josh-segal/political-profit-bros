"""
model01.py is an example of how to access model parameter values that you are storing
in the database and use them to make a prediction when a route associated with prediction is
accessed. 
"""
from backend.db_connection import db
from sklearn.metrics import r2_score
import numpy as np
import logging
from phase3_python_functions import line_of_best_fit, linreg_predict

def train():
  """
  You could have a function that performs training from scratch as well as testing (see below).
  It could be activated from a route for an "administrator role" or something similar. 
  """
  return 'Training the model'

def test():
  return 'Testing the model'


def prediction(stock_df):
  """
  Predicts stock price based on date using simple linear regression 
  """
  X = np.array(stock_df['Date_ordinal'])
  Y = np.array(stock_df['Adj Close'])
  equation = line_of_best_fit(X, Y)
  predict = linreg_predict(X, Y, equation)
  return predict

def predict(var01, var02):
  """
  Retreives model parameters from the database and uses them for real-time prediction
  """
  # get a database cursor 
  cursor = db.get_db().cursor()
  # get the model params from the database
  query = 'SELECT beta_vals FROM model1_params ORDER BY sequence_number DESC LIMIT 1'
  cursor.execute(query)
  return_val = cursor.fetchone()

  params = return_val['beta_vals']
  logging.info(f'params = {params}')
  logging.info(f'params datatype = {type(params)}')

  # turn the values from the database into a numpy array
  params_array = np.array(list(map(float, params[1:-1].split(','))))
  logging.info(f'params array = {params_array}')
  logging.info(f'params_array datatype = {type(params_array)}')

  # turn the variables sent from the UI into a numpy array
  input_array = np.array([1.0, float(var01), float(var02)])
  
  # calculate the dot product (since this is a fake regression)
  prediction = np.dot(params_array, input_array)

  return prediction

  ##############################################################
  
  # # retreive the parameters from the appropriate table
  # cursor.execute('select beta_0, beta_1, beta_2 from model1_param_vals')
  # # fetch the first row from the cursor
  # data = cursor.fetchone()
  # # calculate the predicted result using this functions arguments as well as the model parameter values
  # result = data[0] + int(var01) * data[1] + int(var02) * data[2]

  # # return the result 
  # return result


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
                  'r2':r2
                 }
    return dictionary