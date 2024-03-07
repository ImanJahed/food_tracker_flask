from flask import Blueprint


core_blueprint = Blueprint('core', __name__)


@core_blueprint.route('/')
def index():
    return 'Home Page'