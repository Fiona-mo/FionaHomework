def singleton(func):
    """
    :param func: 这个是单例，后面再了解
    :return:
    """
    _instance = {}

    def wrapper(*args, **kwargs):
        if func not in _instance:
            _instance(func) = func(*args, **kwargs)
        return _instance(func)

    return wrapper()

