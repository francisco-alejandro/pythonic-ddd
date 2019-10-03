from flask import jsonify, abort

from src.container import get_container
from src.user import get_use_cases


def user_controller(http_service=get_container().create('HTTPService')):
    app = http_service.app

    @app.route('/users/<user_id>')
    def get_user(user_id, use_case=get_use_cases().create('GetUseCase')):
        user = use_case.execute(user_id)

        if user is None:
            abort(404, description="User not found")

        return jsonify(user)
