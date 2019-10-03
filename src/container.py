from src.shared.utils import Factory


def get_container():
    from src.shared.infraestructure.services import HTTPService, LoggerService, DBService

    container = Factory()

    container.register_builder('HTTPService', HTTPService)
    container.register_builder('LoggerService', LoggerService)
    container.register_builder('DBService', DBService)

    return container


def register_controllers():
    from src.user.infraestructure.controllers import user_controller
    from src.wallet.infraestructure.controllers import wallet_controller
    from src.shared.infraestructure.controllers import api_controller

    api_controller()
    user_controller()
    wallet_controller()
