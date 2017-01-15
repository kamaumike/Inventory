from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import app_config
from flask_login import LoginManager

# Create an SQLAlchemy object
db = SQLAlchemy()

# Create a LoginManager object
login_manager = LoginManager()


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

    # Initialize the SQLAlchemy object
    db.init_app(app)

    # Initialize the LoginManager object
    login_manager.init_app(app)

    # Redirect users to the login page
    login_manager.login_view = "auth.login"

    return app
