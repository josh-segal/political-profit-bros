########################################################
# Sample customers blueprint of endpoints
# Remove this file if you are not using it in your project
########################################################

from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db
import pandas as pd

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

@stocks.route('/dylan', methods=['GET'])
def stock ():
    cursor = db.get_db().cursor()
    cursor.execute("select concat(ticker, ' - ', company) as item from stock order by ticker")
    theData = cursor.fetchall()
    current_app.logger.info(f'GET /stocks: theData = {pd.DataFrame(theData).values}')
    return jsonify(theData)


    # query = f"select concat(ticker, ' - ', company) from stock order by ticker;'"
    # current_app.logger.info(query)

    # cursor = db.get_db().cursor()
    # cursor.execute(query)
    # the_data = cursor.fetchall()

    # return jsonify(thedata)


@stocks.route('/stock_get/<stock_name>', methods=['GET'])
def get_stock_detail (stock_name):

    query = f"SELECT curr_price, company, ticker, id FROM stock WHERE company like '%{stock_name}' or ticker like '%{stock_name}%'"
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