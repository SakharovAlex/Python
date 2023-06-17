import sys
from functools import wraps


def takes(*args_type):
    def decorator(func):
        @wraps(func)
        def wrapper(*args):
            for arg, arg_type in zip(args, args_type):
                if not isinstance(arg, arg_type):
                    raise TypeError
            return func(*args)
        return wrapper
    return decorator


exec(sys.stdin.read())
