from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db

managers = Blueprint('managers', __name__)

@managers.route('/update', methods=['PUT'])
def update_manager():

    the_data = request.json
    name = the_data['name']
    party = the_data['party']

    query = f""" UPDATE manager SET name = '{name}', party = '{party}' WHERE id = 2;
            """
    current_app.logger.info(query)

    # Execute the query
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'


# Get all the politicians from the database
@managers.route('/politicians', methods=['GET'])
def get_politicians():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of politicians
    cursor.execute('SELECT p.name, p.party, p.state, p.manager_id, p.id FROM politician p LEFT JOIN politician_search_history psh ON p.id = psh.politician_id GROUP BY p.id ORDER BY count(psh.politician_id) LIMIT 5')

    # fetch all the data from the cursor
    theData = cursor.fetchall()
    current_app.logger.info(f'GET /politicians: theData = {theData}')

    return jsonify(theData)


@managers.route('/<politician_name>', methods=['GET'])
def get_stock_detail (politician_name):

    query = f"SELECT p.name, p.party, p.state p.manager_id, p.id FROM politician p WHERE name = '{politician_name}'"
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    the_data = cursor.fetchall()

    return jsonify(the_data)


@managers.route('/track', methods=['POST'])
def put_tracked_politician ():
    
    the_data = request.json
    current_app.logger.info(f'the_data = {the_data}')

    manager_id = the_data['manager_id']
    politician_id = the_data['politician_id']
    candidate_opp = the_data['candidate_opp']
    date = the_data['date']

    query = f"""
            INSERT INTO politician_manager (candidate_opp, manager_id, politician_id, created_at)
            VALUES ('{candidate_opp}', '{manager_id}', '{politician_id}', '{date}')
            """
    current_app.logger.info(query)

    # Execute the query
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'


@managers.route('/politician_portfolio/<manager_id>', methods=['GET'])
def get_politician_portfolio(manager_id):
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of politicians
    cursor.execute(f"SELECT DISTINCT p.name, p.party, p.state, pm.manager_id, p.Politician_Id, pm.candidate_opp FROM politician p JOIN politician_manager pm ON p.Politician_Id = pm.politician_id WHERE pm.manager_id = '{manager_id}'")

    # fetch all the data from the cursor
    theData = cursor.fetchall()
    current_app.logger.info(f'theData = {theData}')
    # for each of the rows, zip the data elements together with
    # the column headers. 

    return jsonify(theData)


@managers.route('/delete_tracked_politician', methods=['DELETE'])
def delete_tracked_politician ():

    the_data = request.json
    politician_id = the_data['politician_id']
    user_id = the_data['user_id']
    candidate_opp = the_data['candidate_opp']

    query = f"""
            DELETE FROM politician_manager WHERE politician_id = '{politician_id}' AND manager_id = '{user_id}' AND candidate_opp = '{candidate_opp}'
            """
    current_app.logger.info(query)

    # Execute the query
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'