from dependency_injector.wiring import Provide
from flask import request, current_app
from flask_restx import Resource
from service.user.auth_service import Auth
from util.decorator import token_required
from util.enum_utils import ConfigEnum

from app.containers import Container
from app.main.dto.dto import RealtimeDto
from app.main.service.realtime_service import RealtimeService

api = RealtimeDto.api

@api.route("")
class RealtimeData(Resource):
    @token_required
    def post(self, realtime_service: RealtimeService=Provide[Container.realtime_service]):
        user_id = Auth.get_user_id_from_token(request)
        admin_key = admin_key = current_app.config["ADMIN_KEY"]
        data = request.json
        realtime_service.publish(user_id, admin_key, data)
        return {
            "code": 1
        }

