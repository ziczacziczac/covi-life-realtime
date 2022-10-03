from dependency_injector import containers, providers
from vijasses.containers import Container

# from service.auth_service import AuthService
from app.main.service.realtime_service import RealtimeService


class RealtimeContainer(Container):
    wiring_config = containers.WiringConfiguration(
        modules=["app.main.controller.realtime_controller"] + Container.modules)

    realtime_service = providers.Factory(
        RealtimeService,
        topic="projects/glassy-totality-324307/topics/realtime-monitor"
    )
