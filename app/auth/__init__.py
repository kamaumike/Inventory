from flask import Blueprint


# Create an instance of Blueprint
auth = Blueprint('auth', __name__)

from . import views
