import os
from src.container import get_container, register_controllers

CONTAINER = get_container()


def main(http_service=get_container().create('HTTPService', name=__name__)):
    register_controllers()

    return http_service.app


if __name__ == "__main__":
    APP = main()

    APP.run(
        debug=True,
        host='0.0.0.0',
        port=int(os.getenv('PORT', '5820')),
    )
