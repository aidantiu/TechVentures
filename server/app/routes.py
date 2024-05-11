"""
This file contains the routes for the Flask app. We can define the routes here.
"""

from app import app, jsonify

#  Index route
@app.route('/')
def index():
    return 'Hello World!'

#  Route to return a JSON response
@app.route('/users', methods=['GET'])
def users():
   return jsonify({'users': ['Aidan', 'Joshua', 'David']})
