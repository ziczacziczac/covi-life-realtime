from flask_restx import Resource

from ..util.dto import Default

api = Default.api


@api.route('/')
class HealthCheck(Resource):
    """
        User Login Resource
    """
    def get(self) :
        return "Hi"