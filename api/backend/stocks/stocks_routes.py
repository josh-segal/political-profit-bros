########################################################
# Sample customers blueprint of endpoints
# Remove this file if you are not using it in your project
########################################################

from flask import Blueprint, request, jsonify, make_response, current_app
import json
import pandas as pd
from backend.db_connection import db

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


@stocks.route('/<stock_name>', methods=['GET'])
def get_stock_detail (stock_name):

    query = f"SELECT * FROM stock WHERE ticker like '%{stock_name}%'"
    # query = f"SELECT curr_price, company id FROM stock WHERE company = '{stock_name}'"
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


@stocks.route('/stocks_dropdown', methods=['GET'])
def stock_dropdown ():

    cursor = db.get_db().cursor()
    cursor.execute("select concat(ticker, ' - ', company) as item from stock order by ticker")
    theData = cursor.fetchall()
    current_app.logger.info(f'GET /stocks: theData = {pd.DataFrame(theData).values}')
    return jsonify(theData)