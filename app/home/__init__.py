from flask import Blueprint


# Create an instance of Blueprint
home = Blueprint('home', __name__)

from . import views
