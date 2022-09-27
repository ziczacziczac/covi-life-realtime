from dependency_injector import containers, providers

from service.device.device_service import DeviceService
from persistent.device.repository.device_repotiory_impl import MongoDeviceRepositoryImpl
from persistent.patient.repository.patient_reposiotry_impl import MongoPatientRepositoryImpl
from persistent.report.repository.gcs_report_file_storage import GCSReportFileStorageRepository
from persistent.report.repository.mongo_record_repository_impl import MongoRecordRepositoryImpl
from persistent.report.repository.mongo_report_repository_impl import MongoReportRepositoryImpl
from persistent.user.repository.mongo_blaclist_token_repository_impl import MongoBlacklistTokenRepositoryImpl
from persistent.user.repository.mongo_opt_log_repository import MongoOTPLogRepositoryImpl
from persistent.user.repository.mongo_otp_verification_repository_impl import MongoOTPVerificationRepository
from persistent.user.repository.mongo_user_repository_impl import MongoUserRepositoryImpl
from service.user.auth_service import Auth
from service.patient.patient_service import PatientService
from service.report.report_service import ReportServiceFactory
from service.user.fcm_noti_service import FirebaseNotificationService
from service.user.sms_service import SMSService
from service.user.user_service import UserService


# from service.auth_service import AuthService
from app.main.service.realtime_service import RealtimeService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=["app.main.controller.realtime_controller",
                                                            "util.decorator"])

    user_repository = providers.Factory(
        MongoUserRepositoryImpl
    )

    blacklist_token_repository = providers.Factory(
        MongoBlacklistTokenRepositoryImpl
    )

    otp_log_repository = providers.Factory(
        MongoOTPLogRepositoryImpl
    )

    otp_verification_repository = providers.Factory(
        MongoOTPVerificationRepository
    )

    sms_service = providers.Factory(
        SMSService,
        env='test',
        otp_verification_repository=otp_verification_repository,
        otp_log_repository=otp_log_repository
    )

    # user_service = providers.Factory(
    #     UserService,
    #     user_repository=user_repository,
    # )

    device_repository = providers.Factory(
        MongoDeviceRepositoryImpl
    )

    device_service = providers.Factory(
        DeviceService,
        device_repository=device_repository
    )

    patient_repository = providers.Factory(
        MongoPatientRepositoryImpl
    )

    report_repository = providers.Factory(
        MongoReportRepositoryImpl
    )

    record_repository = providers.Factory(
        MongoRecordRepositoryImpl
    )

    fcm_noti_service = providers.Factory(
        FirebaseNotificationService,
        user_repository=user_repository,
        patient_repository=patient_repository
    )

    gcs_file_report_repository = providers.Factory(
        GCSReportFileStorageRepository
    )

    gcs_avatar_repository = providers.Factory(
        GCSReportFileStorageRepository,
        bucket_name="globicare_avatar"
    )

    report_service_factory = providers.Factory(
        ReportServiceFactory,
        patient_repository=patient_repository,
        report_repository=report_repository,
        record_repository=record_repository,
        storage_repository=gcs_file_report_repository
    )

    patient_service = providers.Factory(
        PatientService,
        user_repository=user_repository,
        patient_repository=patient_repository,
        record_repository=record_repository,
        storage_repository=gcs_avatar_repository,
        fcm_noti_service=fcm_noti_service
    )

    user_service = providers.Factory(
        UserService,
        user_repository=user_repository,
        sms_service=sms_service,
        storage_repository=gcs_avatar_repository,
        otp_verification_repository=otp_verification_repository
    )

    # patient_service = providers.Factory(
    #     PatientService,
    #     patient_repository=patient_repository
    # )

    # admin_repository = providers.Factory(
    #     MongoAdminRepositoryImpl
    # )
    #
    # blacklist_token_repository = providers.Factory(
    #     MongoBlacklistTokenRepositoryImpl
    # )

    auth_service = providers.Factory(
        Auth,
        user_repository=user_repository,
        sms_service=sms_service,
        otp_verification_repository=otp_verification_repository,
        blacklist_token_repository=blacklist_token_repository
    )

    realtime_service = providers.Factory(
        RealtimeService,
        topic = "projects/glassy-totality-324307/topics/realtime-monitor"
    )
