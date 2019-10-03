import logging

from src.shared.utils import singleton


@singleton
class LoggerService:
    def __init__(self, name=__name__, level=logging.DEBUG):
        logging.basicConfig()
        self._logger = logging.getLogger(name)
        self._logger.setLevel(level)

    @property
    def logger(self):
        return self._logger
