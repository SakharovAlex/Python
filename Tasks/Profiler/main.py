import time


def profiler(func):
    profiler.calls = 0

    def wrapper(*args, **kwargs):
        init_calls = profiler.calls
        profiler.calls += 1
        start = time.time()
        res = func(*args, **kwargs)
        wrapper.calls = profiler.calls - init_calls
        end = time.time()
        wrapper.last_time_taken = end - start
        return res
    wrapper.__doc__ = func.__doc__
    return wrapper
