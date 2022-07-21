import enum


class RequestEnum(enum.Enum):
    FCM_TOKEN = "fcm_token"
    AUTHORIZATION = "Authorization"
    OTP = 'otp'
    PAGE_SIZE = 'page_size'
    PAGE_ID = 'page_id'
    FROM_TS = 'from'
    TO_TS = 'to'
    ORDER_TYPE = 'order'
    USER_PHONE = 'phone'
    USER_NAME = 'name'
    PATIENT_PHONE = 'phone'
    PATIENT_NAME = 'name'
    ORDER_BY = 'order_by'
    DEVICE_SERIAL_NUMBER = "device_serial_number"
    DEVICE_KEY = "device_key"
    FILE = "file"


class ConfigEnum(enum.Enum):
    ECG_REPORT_LINK = "ECG_REPORT_LINK"
    REPORT_TEMP_FOLDER = "REPORT_TEMP_FOLDER"
    TWILIO_ACCOUNT_SID = "TWILIO_ACCOUNT_SID"
    TWILIO_AUTH_TOKEN = "TWILIO_AUTH_TOKEN"
    TWILIO_PHONE_NUMBER = "TWILIO_PHONE_NUMBER"
    FIREBASE_ACCOUNT = "FIREBASE_ACCOUNT"
    DEVICE_SECRET = "DEVICE_SECRET"
    USER_SECRET = "USER_SECRET"
    UPLOAD_FOLDER = "UPLOAD_FOLDER"
    AVATAR_BUCKET = "AVATAR_BUCKET"
    SOCKET_SERVER = "SOCKET_SERVER"
    ADMIN_KEY = "ADMIN_KEY"
    USER_UPLOAD_FOLDER = "USER_UPLOAD_FOLDER"
    USER_AVATAR_BUCKET = "USER_AVATAR_BUCKET"
    ENV = "ENV"
    PASSWORD_ATTEMPT = "PASSWORD_ATTEMPT"
    PASSWORD_RETRY = "PASSWORD_RETRY"
    OTP_ATTEMPT = "PASSWORD_ATTEMPT"
    OTP_RETRY = "OTP_RETRY"
    OTP_SPAM = "OTP_SPAM"
    OTP_SENDER = "OTP_SENDER"
    OTP_KEYWORD = "OTP_KEYWORD"
    OTP_MESSAGE_TEMPLATE = "OTP_MESSAGE_TEMPLATE"
    OTP_SECRET_KEY = "OTP_SECRET_KEY"
    OTP_PARTNER_CODE = "OTP_PARTNER_CODE"
    OTP_LOGGING_TABLE = "OTP_LOGGING_TABLE"


class DeviceEnum(enum.Enum):
    DEVICE_SERIAL_NUMBER = "device_serial_number"
    DEVICE_KEY = "device_key"
    DEVICE_NAME = "device_name"
    IS_DISABLED = "is_disabled"
    DEVICE_ID = "device_id"
    USER_ID = "user_id"
    ACTIVE_AT = "active_at"
    UPDATED_AT = "updated_at"


class OtpEnum(enum.Enum):
    USER_NAME = "user_name"
    USER_PHONE = "user_phone"
    OTP = "otp"
    EXPIRED_AT = "expired_at"
    CREATED_AT = "created_at"
    WRONG_OTP_COUNT = "wrong_otp_count"
    LAST_WRONG_OTP_AT = "last_wrong_otp_at"


class PatientEnum(enum.Enum):
    USER_ID = "user_id"
    USER_PHONE = "user_phone"
    PATIENT_ID = "patient_id"
    PATIENT_NAME = "patient_name"
    HEALTH_INSURANCE_CODE = "health_insurance_code"
    CREATED_AT = "created_at"
    UPDATED_AT = "updated_at"
    IS_DISABLED = "is_disabled"
    DOB = "dob"
    GENDER = "gender"
    CODE = "code"
    ADDRESS = "address"
    TEMP_RANGE = "temp_range"
    HR_RANGE = "hr_range"
    NIBP_RANGE = "nibp_range"
    SPO2_RANGE = "spo2_range"
    PR_RANGE = "pr_range"
    RESP_RANGE = "resp_range"
    ALARM_INTERVAL = "alarm_interval"
    AUTO_SAVE = "auto_save"
    ETHIC = "ethnic"
    RELIGION = "religion"
    RELATION_WITH_ME = "relation_with_me"
    OCCUPATION = "occupation"
    NATIONALITY = "nationality"
    PHONE = "phone"
    IS_DEFAULT = "is_default"
    IMAGE = "image"
    FOLLOWERS = "followers"
    RECORDS = "records"
    RECORD_TEMP = "temp"
    RECORD_HR = "hr"
    RECORD_LOW_PRESSURE = "low_pressure"
    RECORD_HIGH_PRESSURE = "high_pressure"
    RECORD_RESP = "resp"
    RECORD_SPO2 = "spo2"
    RECORD_PR = "pr"
    RECORD_CREATED_AT = "created_at"
    RECORD_ID = "record_id"
    RECORD_LONG = "long"
    RECORD_LAT = "lat"
    AVATAR_LINK = "AVATAR_LINK"
    RECORD_PAYLOAD = "payload"
    RECORD_USER_ID = "user_id"
    RECORD_PATIENT_ID = "patient_id"
    PATIENT_NAMES = "patient_names"
    PATIENTS = "patients"


class UserEnum(enum.Enum):
    USER_ID = "user_id"
    USER_PHONE = "user_phone"
    USER_NAME = "user_name"
    IS_DISABLED = "is_disabled"
    FCM_TOKEN = "fcm_token"
    CREATED_AT = "created_at"
    UPDATED_AT = "updated_at"
    PASSWORD = "password"
    ROLES = "roles"
    IS_LOGGED_IN = "is_logged_in"
    LAST_LOGGED_IN_STATUS = "last_logged_status_at"
    USER_UPDATE_INFO = "user_update_info"
    USER_INFO = "user_info"
    WRONG_PASSWORD_COUNT = "wrong_password_count"
    LAST_PASSWORD_ATTEMPT_AT = "last_password_attempt_at"
    USER_AVATAR_LINK = "USER_AVATAR_LINK"


class MongoEnum(enum.Enum):
    MONGO__ID = "_id"
    MONGO_ID = "id"


class AuthErrorEnum(enum.Enum):
    AUTHORIZATION_REQUIRED = 1001
    INVALID_USER_PHONE = 1002
    INVALID_PASSWORD = 1003
    FCM_DIFFERENT_SENT_OTP_FAILED = 1004
    FCM_DIFFERENT_SENT_OTP_SUCCESS = 1005
    FCM_DIFFERENT_VERIFY_OTP_FAILED = 1006
    INVALID_USER_ID_IN_TOKEN = 1007
    INVALID_TOKEN = 1008
    INVALID_PASSWORD_TOO_MANY_ATTEMPT = 1009
    USER_NOT_FOUND = 1010


class DeviceErrorEnum(enum.Enum):
    INVALID_DEVICE_DATA = 4001
    INVALID_DEVICE = 4002
    SAVE_DEVICE_FAILED = 4003
    DEVICE_EXISTED = 4004
    DEVICE_NOT_FOUND = 4005
    DEVICE_UPDATE_FAILED = 4006
    DEVICE_DELETE_FAILED = 4007
    INVALID_DEVICE_FILE = 4008
    UPLOAD_DEVICE_FAILED = 4009
    SOME_DEVICE_EXISTED = 4010


class PatientErrorEnum(enum.Enum):
    INVALID_PATIENT_DATA = 2001
    PATIENT_EXISTED = 2002
    SAVE_NEW_PATIENT_FAILED = 2003
    GET_PATIENTS_BY_USER_FAILED = 2004
    PATIENT_NOT_FOUND = 2005
    DELETE_PATIENT_FAILED = 2006
    INVALID_PATIENT_UPDATE_DATA = 2007
    UPDATE_PATIENT_FAILED = 2008
    MISSING_PATIENT_IMAGE_FILE = 2009
    UPLOAD_PATIENT_IMAGE_FAILED = 2010
    INVALID_PATIENT_RECORD = 2011
    SAVE_NEW_PATIENT_RECORD_FAILED = 2012
    REMOVE_RECORD_FAILED = 2013
    INVALID_PATIENT_ECG_DATA = 2014
    GET_ECG_REPORT_FAILED = 2015
    ECG_REPORT_NOT_FOUND = 2016
    INVALID_ECG_REPORT = 2017

class UserErrorEnum(enum.Enum):
    INVALID_USER_PHONE = 1001
    INVALID_USER_DATA = 1002
    INVALID_TO_VERIFY_OTP = 1003
    SAVE_NEW_USER_DATA_FAILED = 1004
    WRONG_OTP = 1005
    USER_EXISTED = 1006
    SENT_OTP_FAILED = 1007
    USER_NOT_FOUND = 1008
    PERMISSION_DENIED = 1009
    INVALID_USER_UPDATE_DATA = 1010
    UPDATE_USER_FAILED = 1011
    INVALID_PASSWORD_DATA = 1012
    RESET_PASSWORD_FAILED = 1013
    MISSING_USER_IMAGE_FILE = 1014
    UPLOAD_USER_IMAGE_FAILED = 1015


class OtherErrorEnum(enum.Enum):
    UNHANDLED_EXCEPTION = 5000

class NotificationTypeEnum(enum.Enum):
    SHARE_NOTIFICATION = '2'
    RECORD_NOTIFICATION = '3'
