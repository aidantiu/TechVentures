"""
The __init__.py file is used to initialize the app package. It creates the Flask app instance and imports the routes
"""

from flask import Flask, jsonify
from flask_cors import CORS
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Create the Flask app instance
app = Flask(__name__)

# Load the config file
app.config.from_object(Config)

# Create the database instance
db = SQLAlchemy(app)

# Create the migration engine
migrate = Migrate(app, db)

# Enable CORS
cors = CORS(app)

# Import and register the routes, models
from app import routes, models

