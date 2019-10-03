from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.config.postgres import get_postgres_uri
from src.shared.utils import singleton


@singleton
class DBService:
    def __init__(self):
        self._engine = create_engine(
            get_postgres_uri(),
            isolation_level='SERIALIZABLE',
        )
        self._session = sessionmaker(bind=self._engine)()

    @property
    def session(self):
        return self._session

    @property
    def engine(self):
        return self._engine
