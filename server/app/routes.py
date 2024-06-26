"""
This file contains the routes for the Flask app. We can define the routes here.
"""

from app import app, jsonify
from flask import render_template

#  Index route
@app.route('/')
def index():
    return "Hello, User"

#  Route to return a JSON response
@app.route('/users', methods=['GET'])
def users():
   return jsonify({'users': ['Aidan', 'Joshua', 'David']})
