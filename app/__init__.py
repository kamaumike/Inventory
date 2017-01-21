from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import app_config
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_bootstrap import Bootstrap

# Create an SQLAlchemy object
db = SQLAlchemy()

# Create a LoginManager object
login_manager = LoginManager()

# Create a Bcrypt object
bcrypt = Bcrypt()


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

    # Initialize the Bcrypt object
    bcrypt.init_app(app)

    # Create and initialize the Bootstrap object
    Bootstrap(app)

    # Import & register the admin blueprint
    from .admin import admin
    app.register_blueprint(admin, url_prefix='/admin')

    # Import & register the auth blueprint
    from .auth import auth
    app.register_blueprint(auth)

    # Import & register the home blueprint
    from .home import home
    app.register_blueprint(home)

    return app
