from functools import wraps
from collections import OrderedDict


def cache(size):
    cache_dict = OrderedDict()

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            key = args, tuple(kwargs)
            if key in cache_dict:
                return cache_dict.pop(key)
            else:
                value = func(*args, **kwargs)
                cache_dict[key] = value
                if len(cache_dict) > size:
                    cache_dict.popitem(last=False)
                return value
        return wrapper
    return decorator
