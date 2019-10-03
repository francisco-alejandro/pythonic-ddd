import abc

from src.container import get_container


class GenericRepository(abc.ABC):
    def __init__(self, db_service=get_container().create('DBService')):
        self._session = db_service.session
        self._engine = db_service.engine

    @property
    def session(self):
        return self._session

    @property
    def engine(self):
        return self._engine

    @abc.abstractmethod
    def add(self, entity):
        raise NotImplementedError

    @abc.abstractmethod
    def get_by_id(self, entity_id: str):
        raise NotImplementedError
