from functools import reduce
from typing import Callable, TypeVar
from abc import ABCMeta

T = TypeVar('T')
U = TypeVar('U')


factorial: Callable[[int], int] = lambda x: x * \
    factorial(x - 1) if x > 2 else x

fact: Callable[[int], int] = lambda x: reduce(
    lambda a, b: a * b, (i for i in range(1, x + 1)))


def absurd(a: None) -> T:
    pass


f44: Callable[[], int] = lambda: 44


f_int: Callable[[T], None] = lambda _: None


def f_int_(x: T):
    pass


'''
Two-element set
'''


class Bool(ABCMeta):
    def __init__(self):
        pass


class True_(Bool):
    def __init__(self):
        super().__init__()


class False_(Bool):
    def __init__(self):
        super().__init__()


''' CHALLENGES '''
# Memoization


def memoization(fn: Callable[[T], U]):
    __cache: dict = {}

    def inner(*args: T):
        if args not in __cache:
            print('nuevos valores')
            __cache[args] = fn(*args)
        else:
            print('valores ya cacheados')

        return __cache[args]

    return inner
