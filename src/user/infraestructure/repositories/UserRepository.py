import uuid

from sqlalchemy import Table, Column, String, ForeignKey, MetaData
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import mapper, relationship

from src.shared.utils import singleton
from src.shared.infraestructure.repositories import GenericRepository
from src.user import User
from src.wallet import Wallet, get_repository


@singleton
class UserRepository(GenericRepository):
    def __init__(self, money_repository=get_repository().create('WalletRepository')):
        money_table = money_repository.table

        super().__init__()
        self._metadata = MetaData(self.engine)
        self._table = Table(
            'user',
            self._metadata,
            Column('id', UUID(as_uuid=True), primary_key=True,
                   unique=True, default=uuid.uuid4),
            Column('email', String(255), unique=True, index=True,),
            Column('money_id', UUID(as_uuid=True),
                   ForeignKey(money_table.c.id)),
        )
        self._metadata.create_all()

        mapper(User, self._table, properties={
            'money': relationship(Wallet)
        })

    def add(self, entity: User):
        self.session.add(entity)

    def get_by_id(self, entity_id: str):
        return self.session.query(User).get(entity_id)
