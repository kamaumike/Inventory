from flask import Blueprint


# Create an instance of Blueprint
admin = Blueprint('admin', __name__)

from . import views
