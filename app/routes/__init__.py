from flask import Blueprint

# Initialize blueprint for each module
auth = Blueprint('auth', __name__)
household = Blueprint('household', __name__)
services = Blueprint('services', __name__)
admin = Blueprint('admin', __name__)

# Import routes to register with the blueprints
from . import auth, household, services, admin
