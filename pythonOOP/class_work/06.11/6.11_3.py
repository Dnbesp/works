from math import sin, pi


class Derivate:

    def __init__(self, func):
        self._func = func

    def __call__(self, x):
        dx = 1e-5
        result = (self._func(x + dx) - self._func(x))/dx
        return result


@Derivate
def my_sin(x):
    return round(sin(x), 2)

print(my_sin(pi/2))