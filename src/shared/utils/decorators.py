class _Singleton:
    def __init__(self, cls):
        self._instance = None
        self._cls = cls

    def __call__(self, *args, **kwargs):
        if not self._instance:
            self._instance = self._cls(*args, **kwargs)

        return self._instance


def singleton(cls):
    return _Singleton(cls)
