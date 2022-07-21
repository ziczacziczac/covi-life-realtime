from flask_restx import Namespace, fields

class PatientDto:
    api = Namespace("patients", description='patient related operations')


class AuthDto:
    api = Namespace('auth', description='authentication related operations')

    user_auth = api.model('auth_details', {
        'user_phone': fields.String(required=True, description="The user's phone number address"),
        'password': fields.String(required=True, description='The user password '),
    })

class Default:
    api = Namespace('', description='health check')