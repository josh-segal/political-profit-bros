"""
model01.py is an example of how to access model parameter values that you are storing
in the database and use them to make a prediction when a route associated with prediction is
accessed. 
"""

from backend.db_connection import db
import json

def train():
  """
  You could have a function that performs training from scratch as well as testing (see below).
  It could be activated from a route for an "administrator role" or something similar. 
  """
  return 'Training the model'

def test():
  return 'Testing the model'

def predict(var01, var02):
  """
  Retreives model parameters from the database and uses them for real-time prediction
  """
  # get a cursor 
  cursor = db.get_db().cursor()
  # retreive the parameters from the appropriate table
  cursor.execute('select beta_0, beta_1, beta_2 from model1_param_vals')
  
  # fetch the first row from the cursor
  data = cursor.fetchone()
  # calculate the predicted result using this functions arguments as well as the model parameter values
  result = data[0] + int(var01) * data[1] + int(var02) * data[2]
  # return the result 
  return result