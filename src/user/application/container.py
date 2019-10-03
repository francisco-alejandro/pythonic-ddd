from src.shared.utils import Factory
from .GetUseCase import GetUseCase


def get_use_cases():
    container = Factory()

    container.register_builder('GetUseCase', GetUseCase)

    return container
