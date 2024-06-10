from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db

investors = Blueprint('investors', __name__)

@investors.route('/stock_portfolio/<investor_id>', methods=['GET'])
def get_stock_portfolio(investor_id):
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of stocks
    cursor.execute(f"SELECT DISTINCT s.company, s.ticker FROM stock_unique s JOIN investor_stock ist ON s.ticker = ist.stock_id WHERE investor_id = '{investor_id}'")

    # fetch all the data from the cursor
    theData = cursor.fetchall()
    current_app.logger.info(f'theData = {theData}')
    # for each of the rows, zip the data elements together with
    # the column headers. 

    return jsonify(theData)


@investors.route('/delete_tracked_stock', methods=['DELETE'])
def delete_tracked_stock ():

    the_data = request.json
    stock_id = the_data['stock_id']
    user_id = the_data['user_id']

    query = f"""
            DELETE FROM investor_stock WHERE stock_id = '{stock_id}' AND investor_id = '{user_id}'
            """
    current_app.logger.info(query)

    # Execute the query
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'


@investors.route('/delete_tracked_politician', methods=['DELETE'])
def delete_tracked_politician ():

    the_data = request.json
    politician_id = the_data['politician_id']
    user_id = the_data['user_id']

    query = f"""
            DELETE FROM politician_investor WHERE politician_id = '{politician_id}' AND investor_id = '{user_id}'
            """
    current_app.logger.info(query)

    # Execute the query
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'