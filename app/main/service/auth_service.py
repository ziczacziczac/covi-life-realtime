from covi_model.mongo.user import User
from flask import current_app

from app.main.util.utils import is_valid_uuid
from .user_service import get_user_by_user_id
from ..util.enum_utils import RequestEnum, AuthErrorEnum, ConfigEnum

logged_in_issue = '1'


class Auth:

    @staticmethod
    def get_logged_in_user(new_request):
        # get the auth token
        user_secret = current_app.config[ConfigEnum.USER_SECRET.value]
        try:
            auth_token = new_request.headers.get(RequestEnum.AUTHORIZATION.value).split(" ")[1]
        except:
            response_object = {
                'code': AuthErrorEnum.AUTHORIZATION_REQUIRED.value,
                'message': "Authorization is missing or invalid format"
            }
            return response_object, 401
        if auth_token:
            user_id, _ = User.decode_auth_token(auth_token, user_secret)

            if not is_valid_uuid(user_id):
                response_object = {
                    'code': AuthErrorEnum.INVALID_TOKEN.value,
                    'message': user_id
                }
                return response_object, 401

            user = get_user_by_user_id(user_id)
            if user is None:
                response_object = {
                    'code': AuthErrorEnum.USER_NOT_FOUND.value,
                    'message': "User not found"
                }
                return response_object, 404

            response_object = {
                'code': 1,
                'data': {
                    'user_id': user.user_id,
                    'user_phone': user.user_phone,
                    'roles': user.roles,
                    'registered_on': str(user.created_at)
                }
            }
            return response_object, 200

    @staticmethod
    def get_user_id_from_token(new_request):
        # get the auth token
        user_secret = current_app.config[ConfigEnum.USER_SECRET.value]
        auth_token = new_request.headers.get(RequestEnum.AUTHORIZATION.value).split(" ")[1]
        user_id, _ = User.decode_auth_token(auth_token, user_secret)
        return user_id
