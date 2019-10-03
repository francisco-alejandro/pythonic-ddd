import decimal
from flask import Flask, jsonify
from flask.json import JSONEncoder

from src.shared.utils import singleton

def resource_not_found(error):
    return jsonify(error=str(error)), 404

def unprocessable_request(error):
    return jsonify(error=str(error)), 422

class _DecimalEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        return super(_DecimalEncoder, self).default(o)


@singleton
class HTTPService:
    def __init__(self, name):
        self._app = Flask(name)
        self._app.json_encoder = _DecimalEncoder
        self._app.register_error_handler(404, resource_not_found)
        self._app.register_error_handler(422, unprocessable_request)

    @property
    def app(self):
        return self._app
