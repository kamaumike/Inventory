from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import app_config

# Create an SQLAlchemy object
db = SQLAlchemy()


def create_app(config_name):
    """
    Create an instance of Flask and
    initializes with various configurations
    """

    # Create a Flask instance
    app = Flask(__name__, instance_relative_config=True)

    # Get the environment configurations to load
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    return app
