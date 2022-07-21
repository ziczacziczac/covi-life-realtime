import os
import google.cloud.secretmanager as secretmanager
# uncomment the line below for postgres database url from environment variable
# postgres_local_base = os.environ['DATABASE_URL']

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv('FLASK', 'my_precious_secret_key')
    DEBUG = False
    # Swagger
    RESTX_MASK_SWAGGER = False



class DevelopmentConfig(Config):
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base
    DEBUG = True
    # os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./glassy-totality-324307-0df22e18772f.json"
    project_id = "glassy-totality-324307"

    secret_client = secretmanager.SecretManagerServiceClient()
    avatar_bucket_query = f"projects/{project_id}/secrets/AVATAR_BUCKET/versions/latest"
    firebase_account_query = f"projects/{project_id}/secrets/FIREBASE_SECRET/versions/latest"
    otp_sender_query = f"projects/{project_id}/secrets/OTP_SENDER/versions/latest"
    otp_keyword_query = f"projects/{project_id}/secrets/OTP_KEYWORD/versions/latest"
    otp_message_template_query = f"projects/{project_id}/secrets/OTP_MESSAGE_TEMPLATE/versions/latest"
    otp_secret_key_query = f"projects/{project_id}/secrets/OTP_SECRET_KEY/versions/latest"
    otp_partner_code_query = f"projects/{project_id}/secrets/OTP_PARTNER_CODE/versions/latest"
    otp_logging_table_query = f"projects/{project_id}/secrets/OTP_LOGGING_TABLE/versions/latest"
    admin_key_query = f"projects/{project_id}/secrets/ADMIN_KEY/versions/latest"
    socket_server_query = f"projects/{project_id}/secrets/SOCKET_SERVER/versions/latest"

    ADMIN_KEY = "admin_key"
    SOCKET_SERVER = 'http://127.0.0.1:5000'
    FIREBASE_ACCOUNT = secret_client.access_secret_version(name=firebase_account_query).payload.data.decode("utf-8")
    OTP_SENDER = "OTP_SENDER"
    OTP_KEYWORD = "OTP_KEYWORD"
    OTP_MESSAGE_TEMPLATE = "OTP_KEYWORD"
    OTP_SECRET_KEY = "OTP_SECRET_KEY"
    OTP_PARTNER_CODE = "OTP_SECRET_KEY"
    OTP_LOGGING_TABLE = "OTP_SECRET_KEY"

    DEVICE_SECRET = "123456"
    USER_SECRET = "123456"
    UPLOAD_FOLDER = "."
    PASSWORD_ATTEMPT = 5 #times
    PASSWORD_RETRY = 1 #Minute
    OTP_ATTEMPT = 5 #Times
    OTP_RETRY = 1 #Minute
    OTP_SPAM = 5 #Times
    ENV = "test"
    AVATAR_BUCKET = "iot-user-avatar"
    USER_AVATAR_BUCKET = "iot-user-avatar-2"
    MONGODB_SETTINGS = {
        'host': 'mongodb+srv://admin:pjt7QYnMkurlXyPk@covi-life.rs8zw.mongodb.net/covi-life?retryWrites=true&w=majority',
    }
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    AVATAR_LINK = "http://localhost:5000/patients/{}/image"
    ECG_REPORT_LINK = "http://localhost:5000/patients/{}/records/ecg/{}"
    USER_AVATAR_LINK = "http://localhost:5000/users/{}/image"
    REPORT_TEMP_FOLDER = "C:\\Users\\DELL\\Documents\\dat"

class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'flask_boilerplate_test.db')
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base
    # os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "D:\Python\covi-life\glassy-totality-324307-0df22e18772f.json"
    DEBUG = True
    project_id = "glassy-totality-324307"
    #
    secret_client = secretmanager.SecretManagerServiceClient()
    avatar_bucket_query = f"projects/{project_id}/secrets/AVATAR_BUCKET/versions/latest"
    user_avatar_bucket_query = f"projects/{project_id}/secrets/USER_AVATAR_BUCKET/versions/latest"
    avatar_link_query = f"projects/{project_id}/secrets/AVARTAR_COVI_LIFE/versions/latest"
    user_avatar_link_query = f"projects/{project_id}/secrets/USER_AVARTAR_COVI_LIFE/versions/latest"
    mongo_server_query = f"projects/{project_id}/secrets/MONGO_SERVER/versions/latest"

    firebase_account_query = f"projects/{project_id}/secrets/FIREBASE_SECRET/versions/latest"
    otp_sender_query = f"projects/{project_id}/secrets/OTP_SENDER/versions/latest"
    otp_keyword_query = f"projects/{project_id}/secrets/OTP_KEYWORD/versions/latest"
    otp_message_template_query = f"projects/{project_id}/secrets/OTP_MESSAGE_TEMPLATE/versions/latest"
    otp_secret_key_query = f"projects/{project_id}/secrets/OTP_SECRET_KEY/versions/latest"
    otp_partner_code_query = f"projects/{project_id}/secrets/OTP_PARTNER_CODE/versions/latest"
    otp_logging_table_query = f"projects/{project_id}/secrets/OTP_LOGGING_TABLE/versions/latest"
    user_secret_query = f"projects/{project_id}/secrets/USER_SECRET/versions/latest"
    device_secret_query = f"projects/{project_id}/secrets/DEVICE_SECRET/versions/latest"
    admin_key_query = f"projects/{project_id}/secrets/ADMIN_KEY/versions/latest"
    socket_server_query = f"projects/{project_id}/secrets/SOCKET_SERVER/versions/latest"

    ADMIN_KEY = secret_client.access_secret_version(name=admin_key_query).payload.data.decode("utf-8")
    SOCKET_SERVER = secret_client.access_secret_version(name=socket_server_query).payload.data.decode("utf-8")
    AVATAR_BUCKET = secret_client.access_secret_version(name=avatar_bucket_query).payload.data.decode("utf-8")
    AVATAR_LINK = secret_client.access_secret_version(name=avatar_link_query).payload.data.decode("utf-8")
    USER_AVATAR_BUCKET = secret_client.access_secret_version(name=user_avatar_bucket_query).payload.data.decode("utf-8")
    USER_AVATAR_LINK = secret_client.access_secret_version(name=user_avatar_link_query).payload.data.decode("utf-8")
    MONGO_SERVER = secret_client.access_secret_version(name=mongo_server_query).payload.data.decode("utf-8")
    # DEVICE_SECRET = secret_client.access_secret_version(name=device_secret_query).payload.data.decode("utf-8")
    # USER_SECRET = secret_client.access_secret_version(name=user_secret_query).payload.data.decode("utf-8")
    DEVICE_SECRET = "123456"
    USER_SECRET = "123456"
    FIREBASE_ACCOUNT = secret_client.access_secret_version(name=firebase_account_query).payload.data.decode("utf-8")
    OTP_SENDER = secret_client.access_secret_version(name=otp_sender_query).payload.data.decode("utf-8")
    OTP_KEYWORD = secret_client.access_secret_version(name=otp_keyword_query).payload.data.decode("utf-8")
    OTP_MESSAGE_TEMPLATE = secret_client.access_secret_version(name=otp_message_template_query).payload.data.decode(
        "utf-8")
    OTP_SECRET_KEY = secret_client.access_secret_version(name=otp_secret_key_query).payload.data.decode("utf-8")
    OTP_PARTNER_CODE = secret_client.access_secret_version(name=otp_partner_code_query).payload.data.decode("utf-8")
    OTP_LOGGING_TABLE = secret_client.access_secret_version(name=otp_logging_table_query).payload.data.decode("utf-8")
    UPLOAD_FOLDER = "."
    PASSWORD_ATTEMPT = 5 #times
    PASSWORD_RETRY = 1 #Minute
    OTP_ATTEMPT = 5 #Times
    OTP_RETRY = 1 #Minute
    OTP_SPAM = 500 #Times
    # ENV = "production"
    ENV = "test"
    REPORT_TEMP_FOLDER = "/tmp"
    MONGODB_SETTINGS = {
        'host': MONGO_SERVER,
    }
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    ECG_REPORT_LINK = "https://covi-life-djgdyxgtha-el.a.run.app/patients/{}/records/ecg/{}"


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY