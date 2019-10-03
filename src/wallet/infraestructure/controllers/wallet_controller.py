from flask import abort, request

from src.container import get_container
from src.wallet.application import get_use_cases


def wallet_controller(http_service=get_container().create('HTTPService')):
    app = http_service.app

    @app.route('/wallets/transfer', methods=['POST'])
    def post_transfer(create_transfer_use_case=get_use_cases().create('CreateTransferUseCase')):
        content = request.get_json(silent=True)
        try:
            create_transfer_use_case.execute(
                origin_user_id=content.get('originUserId'),
                target_user_id=content.get('targetUserId'),
                amount=content.get('amount')
            )

            return '', 204
        except Exception as error:
            abort(422, description=error)
