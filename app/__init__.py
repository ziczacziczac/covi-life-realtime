
from flask_restx import Api
from flask import Blueprint
from .main.controller.realtime_controller import api as realtime_ns

blueprint = Blueprint('api', __name__)

api = Api(
    blueprint,
    title='COVI-LIFE Realtime Server',
    version='1.0',
    description='COVI-LIFE Realtime Server',
    # authorizations=authorizations,
    security='apikey'
)

api.add_namespace(realtime_ns, path='/realtime')
