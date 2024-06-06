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
