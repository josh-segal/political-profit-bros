from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db

investors = Blueprint('investors', __name__)

@investors.route('/stock_portfolio/<investor_id>', methods=['GET'])
def get_stock_portfolio(investor_id):
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of stocks
    cursor.execute(f"SELECT DISTINCT s.company, s.id FROM stock s JOIN investor_order io ON s.id = io.stock_id AND io.buy = 1 WHERE investor_id = '{investor_id}'")

    # fetch all the data from the cursor
    theData = cursor.fetchall()
    current_app.logger.info(f'theData = {theData}')
    # for each of the rows, zip the data elements together with
    # the column headers. 

    return jsonify(theData)