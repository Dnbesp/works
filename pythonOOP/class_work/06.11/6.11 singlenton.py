def singleton(orig_cls):
    orig_new = orig_cls.__new__
    instance = None


    def __new__(cls, *args, **qwargs):
        nonlocal instance
        if instance is None:
            instance = orig_new(cls, *args, **qwargs)
            return instance
        orig_cls.__new__ = __new__
        return orig_cls


    @singleton
    class Logger:
        def log(msg):
            print(msg)


    logger1 = Logger()
    logger2 = Logger()
    assert logger1 is logger2
