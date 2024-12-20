from flask import Blueprint, request, jsonify, make_response, current_app
import json
import pymysql
from backend.db_connection import db
import pandas as pd
from backend.ml_models.model01 import volume_prediction
politicians = Blueprint('politicians', __name__)


# Get all the politicians from the database
@politicians.route('/politicians', methods=['GET'])
def get_politicians():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of politicians
    cursor.execute('''SELECT p.name, p.party, p.state, p.id
FROM politician p
         LEFT JOIN politician_search_history psh ON p.id = psh.politician_id
GROUP BY p.id, p.name, p.party, p.state
ORDER BY count(psh.politician_id)
LIMIT 10''')

    # fetch all the data from the cursor
    theData = cursor.fetchall()
    current_app.logger.info(f'GET /politicians: theData = {theData}')

    return jsonify(theData)


@politicians.route('/politicians_all', methods=['GET'])
def get_all_politicians():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of politicians
    cursor.execute('''SELECT p.name, p.party, p.state, p.id
FROM politician p
                   ''')

    # fetch all the data from the cursor
    theData = cursor.fetchall()
    current_app.logger.info(f'GET /politicians_all: theData = {theData}')

    return jsonify(theData)


@politicians.route('/<politician_name>', methods=['GET'])
def get_stock_detail (politician_name):

    query = f"SELECT p.name, p.party, p.state, p.id FROM politician p WHERE name like '%{politician_name}%'"
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    the_data = cursor.fetchall()

    return jsonify(the_data)


from flask import request, jsonify

@politicians.route('/legislations', methods=['POST'])
def get_politician_name():
    politician_ids = request.json
    
    if not politician_ids:
        return jsonify({"error": "No politician IDs provided"}), 400

    # Convert politician_ids to a comma-separated string
    ids_str = ','.join([f'"{id}"' for id in politician_ids])

    query = f"""
        SELECT id, name, party, state 
        FROM politician 
        WHERE id IN ({ids_str})
    """
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    the_data = cursor.fetchall()

    return jsonify(the_data)





@politicians.route('/track', methods=['POST'])
def put_tracked_politician ():
    
    the_data = request.json
    current_app.logger.info(f'the_data = {the_data}')

    investor_id = the_data['investor_id']
    politician_id = the_data['politician_id']
    date = the_data['date']

    query = f"""
            INSERT INTO politician_investor (investor_id, politician_id, created_at)
            VALUES ('{investor_id}', '{politician_id}', '{date}')
            """
    current_app.logger.info(query)

    # Execute the query
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'



@politicians.route('/politician_portfolio/<investor_id>', methods=['GET'])
def get_politician_portfolio(investor_id):
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of stocks
    cursor.execute(f"SELECT DISTINCT p.name, p.party, p.state, p.id FROM politician p JOIN politician_investor po ON p.id = po.politician_id WHERE investor_id = '{investor_id}'")

    # fetch all the data from the cursor
    theData = cursor.fetchall()
    current_app.logger.info(f'theData = {theData}')
    # for each of the rows, zip the data elements together with
    # the column headers. 

    return jsonify(theData)

@politicians.route('/distinct_politicians', methods=['GET'])
def get_distinct_politicians():
    current_app.logger.info('politicians_routes.py: GET /politicians route')
    cursor = db.get_db().cursor()
    query = f"SELECT DISTINCT(Name) FROM politician ORDER BY Name"
    cursor.execute(query)
    current_app.logger.info(f'Query: {query}')
    theData = cursor.fetchall()
    current_app.logger.info(f'fetchall: {theData}') 
    return jsonify(theData)

@politicians.route('/volume_politicians/<name>', methods=['GET'])
def get_politician_trade_volume(name):
    current_app.logger.info('politicians_routes.py: GET /volume_politicians/<name> route')
    cursor = db.get_db().cursor()
    current_app.logger.info(f'politician name = {name}')
    query = f"SELECT Name, Party, Date_Traded, SUM(Trade_Value) AS Total_Trade_Value \
            FROM poly_trade_data \
            WHERE Name LIKE '%{name}%' \
            GROUP BY Name, Party, Date_Traded \
            ORDER BY SUM(Trade_Value) DESC" 
    cursor.execute(query)
    current_app.logger.info(f'Query: {query}')
    theData = cursor.fetchall()
    current_app.logger.info(f'fetchall: {theData}') 
    return jsonify(theData)


@politicians.route('/politicians_volume', methods=['GET'])
def get_politician_by_volume ():
    cursor = db.get_db().cursor()
    query = """
SELECT p.name, p.party, p.state, p.id, SUM(pt.Trade_Value) AS Total_Trade_Value
FROM politician p
         JOIN
     politician_trade pt ON p.id = pt.id
GROUP BY p.name, p.party, p.state, p.id
ORDER BY Total_Trade_Value DESC
LIMIT 10;
""" 
    cursor.execute(query)
    current_app.logger.info(f'Query: {query}')
    theData = cursor.fetchall()
    current_app.logger.info(f'fetchall: {theData}') 
    return jsonify(theData)


@politicians.route('/predict_volume/<name>', methods=['GET'])
def predict_trade_volume(name):
    current_app.logger.info('politicians_routes.py: GET /predict_volume/<name> route')
    current_app.logger.info(f'name = {name}')
    predict_values = volume_prediction(name)
    return_dict = {'result': predict_values}
    the_response = make_response(jsonify(return_dict))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

@politicians.route('/politicians_dropdown', methods=['GET'])
def politician_dropdown ():
    cursor = db.get_db().cursor()
    cursor.execute("select distinct concat(Name, ' - ', Party, ' - ', State) as item, p.name, p.party, p.state, p.id FROM poly_trade_data p order by item")
    theData = cursor.fetchall()
    current_app.logger.info(f'GET /politician: theData = {pd.DataFrame(theData).values}')
    return jsonify(theData)



@politicians.route('/politician_stock_details/<politician_name>', methods=['GET'])
def get_politician_stock_detail (politician_name):

    query = f"SELECT * FROM poly_trade_data WHERE Name like '%{politician_name}%'"
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    the_data = cursor.fetchall()

    return jsonify(the_data)


@politicians.route('/politician_trade', methods=['GET'])
def get_politician_trade_detail ():

    query = f"SELECT * FROM politician_trade"
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    the_data = cursor.fetchall()

    return jsonify(the_data)


@politicians.route('/politician_trade_party_date/<date>', methods=['GET'])
def get_politician_trade_detail_party_date (date):

    query = f"""
SELECT *
FROM politician_trade
WHERE Asset_Type = 'Stock'
    AND Date_Traded BETWEEN DATE_SUB('{date}', INTERVAL 1 MONTH) AND DATE_ADD('{date}', INTERVAL 1 MONTH)
ORDER BY Trade_Value DESC
LIMIT 3;
    """
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    the_data = cursor.fetchall()

    return jsonify(the_data)