import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Secret key for signing cookies
    SECRET_KEY = os.environ.get('SECRET KEY') or 'hard to guess string'

    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')