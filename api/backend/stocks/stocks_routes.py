from flask import Blueprint, request, jsonify, make_response, current_app
import json
import pandas as pd
from backend.db_connection import db
import yfinance as yf
from datetime import date
from dateutil.relativedelta import *


stocks = Blueprint('stocks', __name__)

# Get all the stocks from the database
@stocks.route('/stocks', methods=['GET'])
def get_stocks():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of stocks
    cursor.execute('SELECT s.curr_price, s.company, s.ticker, s.id FROM stock s LEFT JOIN stock_search_history ssh ON s.id = ssh.stock_id GROUP BY s.id ORDER BY count(ssh.stock_id) DESC LIMIT 10')

    # fetch all the data from the cursor
    theData = cursor.fetchall()
    current_app.logger.info(f'GET /stocks: theData = {theData}')

    return jsonify(theData)


# @stocks.route('/stocks/<name>', methods=['GET'])
# def predict_stockprice(name):
#     current_app.logger.info(f'name: {name}')
#     current_date = date.today()
#     current_date_str = current_date.strftime('%Y-%m-%d')
#     current_app.logger.info(f'today date: {current_date_str}')

#     begin_date = current_date - relativedelta(months=+12)
#     begin_date_str = begin_date.strftime('%Y-%m-%d')
#     current_app.logger.info(f'begin date: {begin_date_str}')

#     ### Add some sort of if statement to check if the stock was even searched up in the database
#         ### If there is data, then do SELECT statement,
#         ### If not then, use the yfinance to download df and then transform that into insert statements

#     stock_data = yf.download([f'{name}'], start=begin_date_str, end=current_date_str).reset_index()
#     # Convert dates to ordinal numbers to ensure striaght linear regression
#     stock_data['Date_ordinal'] = stock_data['Date'].apply(lambda date: date.toordinal())


#     predict_values = prediction(stock_data)
#     return stock_data, predict_values

#jsonify dictionary



# # Get all customers from the DB based on name
# @politicians.route('/politicians/<name>', methods=['GET'])
# def get_politicians(name):
#     current_app.logger.info('politicians_routes.py: GET /politicians/<name> route')
#     cursor = db.get_db().cursor()
#     current_app.logger.info(f'politician name = {name}')
#     query = f"SELECT * FROM politician WHERE name like '%{name}%'"
#     cursor.execute(query)
#     current_app.logger.info(f'Query: {query}')
#     theData = cursor.fetchall()
#     current_app.logger.info(f'fetchall: {theData}') 
#     return jsonify(theData)


#     if name_input:
#     try:
#         # URL encode the name_input to handle spaces and special characters
#         encoded_name = urllib.parse.quote(name_input)
#         logger.info(f'encoded_name: {encoded_name}')
#         response = requests.get(f'http://api:4000/po/politicians/{encoded_name}') 
#         logger.info(f'byebyebyebye{response}')
#         results = response.json()
#         st.dataframe(results, column_order=["Name", "Politician_id", "Party", "Chamber", "State", "Asset_Type", \
#          "Issuer", "Ticker", "Issuer_Country", "Type", "txId", "Date_Traded", "Date_Published", "Trade_Size",\
#              "Trade_Price", "Trade_Value"])
#     except requests.exceptions.RequestException as e:
#         st.error(f"An error occurred: {e}")



@stocks.route('/<stock_name>', methods=['GET'])
def get_stock_detail (stock_name):

    query = f"SELECT * FROM stock WHERE ticker like '%{stock_name}%'"
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    the_data = cursor.fetchall()

    return jsonify(the_data)


@stocks.route('/track', methods=['POST'])
def put_tracked_stock ():
    
    the_data = request.json
    current_app.logger.info(f'the_data = {the_data}')

    investor_id = the_data['investor_id']
    stock_id = the_data['stock_id']
    date = the_data['date']

    query = f"""
            INSERT INTO investor_stock (investor_id, stock_id, created_at)
            VALUES ('{investor_id}', '{stock_id}', '{date}')
            """
    
    current_app.logger.info(query)

    # Execute the query
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'


@stocks.route('/history', methods=['POST'])
def put_history_stock ():
    
    the_data = request.json
    current_app.logger.info(f'the_data = {the_data}')

    investor_id = the_data['investor_id']
    stock_id = the_data['stock_id']
    date = the_data['date']

    query = f"""
            INSERT INTO stock_search_history (investor_id, stock_id, date)
            VALUES ('{investor_id}', '{stock_id}', '{date}')
            """
    
    current_app.logger.info(query)

    # Execute the query
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'


@stocks.route('/stocks_dropdown', methods=['GET'])
def stock_dropdown ():

    cursor = db.get_db().cursor()
    cursor.execute("select concat(ticker, ' - ', company) as item from stock order by ticker")
    theData = cursor.fetchall()
    current_app.logger.info(f'GET /stocks: theData = {pd.DataFrame(theData).values}')
    return jsonify(theData)