from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db

politicians = Blueprint('politicians', __name__)

# Get all the politicians from the database
@politicians.route('/politicians', methods=['GET'])
def get_politicians():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of politicians
    cursor.execute('SELECT p.name, p.party, p.state, p.chamber, p.manager_id, p.id FROM politician p LEFT JOIN politician_search_history psh ON p.id = psh.politician_id GROUP BY p.id ORDER BY count(psh.politician_id) LIMIT 5')

    # fetch all the data from the cursor
    theData = cursor.fetchall()
    current_app.logger.info(f'GET /politicians: theData = {theData}')

    return jsonify(theData)


@politicians.route('/<politician_name>', methods=['GET'])
def get_stock_detail (politician_name):

    query = f"SELECT p.name, p.party, p.state, p.chamber, p.manager_id, p.id FROM politician p WHERE name = '{politician_name}'"
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
    cursor.execute(f"SELECT DISTINCT p.name, p.party, p.state, p.chamber, p.manager_id, p.id FROM politician p JOIN politician_investor po ON p.id = po.politician_id WHERE investor_id = '{investor_id}'")

    # fetch all the data from the cursor
    theData = cursor.fetchall()
    current_app.logger.info(f'theData = {theData}')
    # for each of the rows, zip the data elements together with
    # the column headers. 

    return jsonify(theData)