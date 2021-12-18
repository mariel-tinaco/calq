import functools
from typing import Callable, Union
from numpy import ndarray

ComposableFunction = Callable[[Union(complex, int, float, ndarray)], Union(complex, int, float, ndarray)]

def compose_fn(*functions : ComposableFunction) -> ComposableFunction:
    return functools.reduce(lambda f, g: lambda x: g(f(x)), functions)