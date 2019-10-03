from src.shared.utils import singleton
from src.user.infraestructure.repositories import get_repository
from src.user.application import get_use_cases


class ValidationError(Exception):
    pass


@singleton
class CreateTransferUseCase:
    def __init__(
        self,
        user_repository=get_repository().create('UserRepository'),
        get_user_use_case=get_use_cases().create('GetUseCase'),
    ):
        self._user_repository = user_repository
        self._get_user_use_case = get_user_use_case

    def _validate(self, origin_user, target_user, amount):
        if not amount or amount < 0:
            raise ValueError('amount should be positive')

        if not origin_user:
            raise ValidationError('Not origin user found')

        if not origin_user:
            raise ValidationError('Not target user found')

        if origin_user.money < amount:
            raise ValidationError('No funds')

        return origin_user, target_user, amount

    def execute(self, origin_user_id, target_user_id, amount):
        origin_user, target_user, amount = self._validate(
            origin_user=self._get_user_use_case.execute(origin_user_id),
            target_user=self._get_user_use_case.execute(target_user_id),
            amount=amount
        )

        origin_user.money -= amount
        target_user.money += amount

        self._user_repository.session.commit()
