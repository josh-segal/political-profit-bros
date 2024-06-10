from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db

legislations = Blueprint('legislations', __name__)

@legislations.route('/legislations', methods=['GET'])
def get_legislations ():

    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of politicians
    cursor.execute("""
                   
SELECT Title, Sponsor, Party_of_Sponsor, Date_of_Introduction, Subject
                   FROM legislation_mega

                   """)

    # fetch all the data from the cursor
    theData = cursor.fetchall()
    current_app.logger.info(f'GET /legislations: theData = {theData}')

    return jsonify(theData)