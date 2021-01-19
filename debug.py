from functools import partial, wraps
def debug(func=None,*,prefix=''):
    if func is None:
        return partial(debug,prefix=prefix)
    def wrapper(*args, **kwargs):
        print(prefix+func.__name__)
        return func(*args,**kwargs)
    return wrapper
