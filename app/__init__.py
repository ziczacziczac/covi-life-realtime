
from flask_restx import Api
from flask import Blueprint
from .main.controller.patient_controller import api as patient_ns
from .main.controller.healtcheck_controller import api as health_ns

blueprint = Blueprint('api', __name__)

api = Api(
    blueprint,
    title='FLASK RESTPLUS(RESTX) API BOILER-PLATE WITH JWT',
    version='1.0',
    description='a boilerplate for flask restplus (restx) web service',
    # authorizations=authorizations,
    security='apikey'
)

api.add_namespace(patient_ns, path='/patients')
api.add_namespace(health_ns, path='/')
