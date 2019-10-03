from src.shared.utils import singleton
from src.user.infraestructure.repositories import get_repository


@singleton
class GetUseCase:
    def __init__(self, user_repository=get_repository().create('UserRepository')):
        self._user_repository = user_repository

    def execute(self, user_id):
        return self._user_repository.get_by_id(entity_id=user_id)
