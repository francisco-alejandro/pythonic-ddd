from src.shared.utils import Factory
from .CreateTransferUseCase import CreateTransferUseCase


def get_use_cases():
    container = Factory()

    container.register_builder('CreateTransferUseCase', CreateTransferUseCase)

    return container
