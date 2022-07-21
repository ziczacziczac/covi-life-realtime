from flask import request, current_app
from flask_restx import Resource

from app.main.service.auth_service import Auth
from app.main.service.realtime_service import send_message_to_topic
from app.main.util.decorator import token_required
from app.main.util.dto import PatientDto
from app.main.util.enum_utils import ConfigEnum

api = PatientDto.api


@api.route("/realtime")
class PatientRealtime(Resource):
    @token_required
    def post(self):
        user_id = Auth.get_user_id_from_token(request)
        record = request.json
        admin_key = current_app.config[ConfigEnum.ADMIN_KEY.value]
        socket_server = current_app.config[ConfigEnum.SOCKET_SERVER.value]
        try:
            send_message_to_topic(user_id, record, admin_key, socket_server)
            return {
                "code": 1
            }, 200
        except Exception as e:
            print(e)
            return {
                "code": 5000,
                "message": str(e)
            }