from typing import TypeVar, Tuple, NewType

A = TypeVar('A')
B = TypeVar('B')
C = TypeVar('C')


def swap(p: Tuple[A, B]) -> Tuple[B, A]:
    a, b = p

    return (b, a)  # (p[1], p[0])


def alpha(t: Tuple[Tuple[A, B], C]) -> Tuple[A, Tuple[B, C]]:
    [a, b], c = t

    return (a, (b, c))
