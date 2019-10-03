from src.shared.utils import Factory
from .UserRepository import UserRepository


def get_repository():
    container = Factory()

    container.register_builder('UserRepository', UserRepository)

    return container
