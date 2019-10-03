import uuid

from sqlalchemy import Table, Column, String, Numeric, MetaData
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import mapper

from src.shared.utils import singleton
from src.shared.infraestructure.repositories import GenericRepository
from src.wallet import Wallet


@singleton
class WalletRepository(GenericRepository):
    def __init__(self):
        super().__init__()

        self._metadata = MetaData(self.engine)
        self._table = Table(
            'wallet',
            self._metadata,
            Column('id', UUID(as_uuid=True), primary_key=True,
                   unique=True, default=uuid.uuid4),
            Column('currency', String(3)),
            Column('value', Numeric),
        )
        self._metadata.create_all()

        mapper(Wallet, self._table)

    @property
    def table(self):
        return self._table

    def add(self, entity: Wallet):
        self.session.add(entity)

    def get_by_id(self, entity_id: str):
        pass
