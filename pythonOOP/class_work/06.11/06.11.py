from typing import Callable


def star(n: int):
    def new_decorate(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            """docstring wrapper"""
            print('*'*n)
            func(*args, **kwargs)
            print('*'*n)
        return wrapper
    return new_decorate


@star(5)
def f1(x):
    """docstring f1"""
    print(f"Call f1 = {x**2}")


f1(3)
print(f1.__name__)
print(f1.__doc__)