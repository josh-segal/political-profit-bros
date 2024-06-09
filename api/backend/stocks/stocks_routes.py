from flask import Blueprint, request, jsonify, make_response, current_app
import json
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
    cursor.execute('SELECT s.curr_price, s.company, s.ticker, s.id FROM stock s LEFT JOIN stock_search_history ssh ON s.id = ssh.stock_id GROUP BY s.id ORDER BY count(ssh.stock_id) LIMIT 5')

    # fetch all the data from the cursor
    theData = cursor.fetchall()
    current_app.logger.info(f'GET /stocks: theData = {theData}')

    return jsonify(theData)
"""

@stocks.route('/stocks/<name>', methods=['GET'])
def predict_stockprice(name):
    current_app.logger.info(f'name: {name}')
    current_date = date.today()
    current_date_str = current_date.strftime('%Y-%m-%d')
    current_app.logger.info(f'today date: {current_date_str}')

    begin_date = current_date - relativedelta(months=+12)
    begin_date_str = begin_date.strftime('%Y-%m-%d')
    current_app.logger.info(f'begin date: {begin_date_str}')

    ### Add some sort of if statement to check if the stock was even searched up in the database
        ### If there is data, then do SELECT statement,
        ### If not then, use the yfinance to download df and then transform that into insert statements

    stock_data = yf.download([f'{name}'], start=begin_date_str, end=current_date_str).reset_index()
    # Convert dates to ordinal numbers to ensure striaght linear regression
    stock_data['Date_ordinal'] = stock_data['Date'].apply(lambda date: date.toordinal())


    predict_values = prediction(stock_data)
    return stock_data, predict_values

#jsonify dictionary

"""
"""
# Get all customers from the DB based on name
@politicians.route('/politicians/<name>', methods=['GET'])
def get_politicians(name):
    current_app.logger.info('politicians_routes.py: GET /politicians/<name> route')
    cursor = db.get_db().cursor()
    current_app.logger.info(f'politician name = {name}')
    query = f"SELECT * FROM politician WHERE name like '%{name}%'"
    cursor.execute(query)
    current_app.logger.info(f'Query: {query}')
    theData = cursor.fetchall()
    current_app.logger.info(f'fetchall: {theData}') 
    return jsonify(theData)


    if name_input:
    try:
        # URL encode the name_input to handle spaces and special characters
        encoded_name = urllib.parse.quote(name_input)
        logger.info(f'encoded_name: {encoded_name}')
        response = requests.get(f'http://api:4000/po/politicians/{encoded_name}') 
        logger.info(f'byebyebyebye{response}')
        results = response.json()
        st.dataframe(results, column_order=["Name", "Politician_id", "Party", "Chamber", "State", "Asset_Type", \
         "Issuer", "Ticker", "Issuer_Country", "Type", "txId", "Date_Traded", "Date_Published", "Trade_Size",\
             "Trade_Price", "Trade_Value"])
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {e}")



"""

@stocks.route('/<stock_name>', methods=['GET'])
def get_stock_detail (stock_name):

    query = f"SELECT curr_price, company id FROM stock WHERE company = '{stock_name}'"
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    the_data = cursor.fetchall()

    return jsonify(the_data)


@stocks.route('/track', methods=['POST'])
def put_tracked_stock ():
    
    the_data = request.json
    current_app.logger.info(f'the_data = {the_data}')

    # price = the_data['price']
    # buy = the_data['buy']
    # stock_id = the_data['stock_id']
    # investor_id = the_data['investor_id']
    # volume = the_data['volume']
    # date = the_data['date']

    # query = f"""
    #         INSERT INTO investor_order (price, buy, stock_id, investor_id, volume, date)
    #         VALUES ({price}, {buy}, {stock_id}, {investor_id}, {volume}, '{date}')
    #         """

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


# @stocks.route('/product/<id>', methods=['GET'])
# def get_product_detail (id):

#     query = 'SELECT id, product_name, description, list_price, category from stock WHERE id = ' + str(id)
#     current_app.logger.info(query)

#     cursor = db.get_db().cursor()
#     cursor.execute(query)
#     column_headers = [x[0] for x in cursor.description]
#     json_data = []
#     the_data = cursor.fetchall()
#     for row in the_data:
#         json_data.append(dict(zip(column_headers, row)))
#     return jsonify(json_data)
    

# # get the top 5 stocks from the database
# @stocks.route('/mostExpensive')
# def get_most_pop_stocks():
#     cursor = db.get_db().cursor()
#     query = '''
#         SELECT product_code, product_name, list_price, reorder_level
#         from stock
#         ORDER BY list_price DESC
#         LIMIT 5
#     '''
#     cursor.execute(query)
#     # grab the column headers from the returned data
#     column_headers = [x[0] for x in cursor.description]

#     # create an empty dictionary object to use in 
#     # putting column headers together with data
#     json_data = []

#     # fetch all the data from the cursor
#     theData = cursor.fetchall()

#     # for each of the rows, zip the data elements together with
#     # the column headers. 
#     for row in theData:
#         json_data.append(dict(zip(column_headers, row)))

#     return jsonify(json_data)


# @stocks.route('/tenMostExpensive', methods=['GET'])
# def get_10_most_expensive_stocks():
    
#     query = '''
#         SELECT product_code, product_name, list_price, reorder_level
#         from stock
#         ORDER BY list_price DESC
#         LIMIT 10
#     '''

#     cursor = db.get_db().cursor()
#     cursor.execute(query)

#     column_headers = [x[0] for x in cursor.description]

#     # create an empty dictionary object to use in 
#     # putting column headers together with data
#     json_data = []

#     # fetch all the data from the cursor
#     theData = cursor.fetchall()

#     # for each of the rows, zip the data elements together with
#     # the column headers. 
#     for row in theData:
#         json_data.append(dict(zip(column_headers, row)))
    
#     return jsonify(json_data)

# @stocks.route('/product', methods=['POST'])
# def add_new_product():
    
#     # collecting data from the request object 
#     the_data = request.json
#     current_app.logger.info(the_data)

#     #extracting the variable
#     name = the_data['product_name']
#     description = the_data['product_description']
#     price = the_data['product_price']
#     category = the_data['product_category']

#     # Constructing the query
#     query = 'insert into stocks (product_name, description, category, list_price) values ("'
#     query += name + '", "'
#     query += description + '", "'
#     query += category + '", '
#     query += str(price) + ')'
#     current_app.logger.info(query)

#     # executing and committing the insert statement 
#     cursor = db.get_db().cursor()
#     cursor.execute(query)
#     db.get_db().commit()
    
#     return 'Success!'

# ### Get all product categories
# @stocks.route('/categories', methods = ['GET'])
# def get_all_categories():
#     query = '''
#         SELECT DISTINCT category AS label, category as value
#         from stock
#         WHERE category IS NOT NULL
#         ORDER BY category
#     '''

#     cursor = db.get_db().cursor()
#     cursor.execute(query)

#     json_data = []
#     # fetch all the column headers and then all the data from the cursor
#     column_headers = [x[0] for x in cursor.description]
#     theData = cursor.fetchall()
#     # zip headers and data together into dictionary and then append to json data dict.
#     for row in theData:
#         json_data.append(dict(zip(column_headers, row)))
    
#     return jsonify(json_data)

# @stocks.route('/product', methods = ['PUT'])
# def update_product():
#     product_info = request.json
#     current_app.logger.info(product_info)

#     return "Success"