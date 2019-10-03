from src.shared.utils import Factory
from .WalletRepository import WalletRepository


def get_repository():
    container = Factory()

    container.register_builder('WalletRepository', WalletRepository)

    return container
