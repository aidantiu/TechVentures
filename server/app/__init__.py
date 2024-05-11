"""
The __init__.py file is used to initialize the app package. It creates the Flask app instance and imports the routes
"""

from flask import Flask, jsonify
from flask_cors import CORS

# Create the Flask app instance
app = Flask(__name__)

# Enable CORS
cors = CORS(app)

# Import and register the routes
from app import routes

