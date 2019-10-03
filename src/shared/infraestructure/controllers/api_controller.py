from src.container import get_container


def api_controller(http_service=get_container().create('HTTPService')):
    app = http_service.app

    @app.route('/')
    def health_check():
        return 'ping'
