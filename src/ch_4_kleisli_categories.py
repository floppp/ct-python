from math import sqrt
from typing import Callable, TypeVar, Tuple, Generic, NewType, Union


T = TypeVar('T')
A = TypeVar('A')
B = TypeVar('B')
C = TypeVar('C')


''' WRITER '''
# Writer = NewType('Writer', Tuple[T, str])


class Writer(Generic[T]):
    def __init__(self, t: T, s: str):
        self.t = t
        self.s = s


# La composición de este tipo es tal que
# (>=>) :: (a -> Writer b) -> (b -> Writer c) -> (a -> Writer c)
# def >=>[A, B, C](m1: A => Writer[B], m2: B => Writer[C]): A => Writer[C]


def writer_composition(fa: Callable[[A], Writer[B]],
                       fb: Callable[[B], Writer[C]]) -> Callable[[A], Writer[C]]:
    def inner(arg: A) -> Writer[C]:
        wb: Writer[B] = fa(arg)
        wc: Writer[C] = fb(wb.t)

        # T ha implementar el 'dunder method' `__add__`
        return Writer(wc.t, wb.s + wb.s)

    return inner


''' CHALLENGES '''


# Ejercicio 1
class Option(Generic[T]):
    def __init__(self, v: Union[T, None]):
        self.v = v

    def identity(self) -> Union[T, None]:
        return self.v

    def is_valid(self):
        return self.v is not None


def optional_composition(fa: Callable[[A], Option[B]],
                         fb: Callable[[B], Option[C]]) -> Callable[[A], Option[C]]:
    def inner(arg: A) -> Option[C]:
        wb: Option[B] = fa(arg)
        # Si usamos is_valid nos da problemas mypy, así que mejor así.
        return fb(wb.v) if wb.v else Option(None)

    return inner


# Ejercicio 2
# TODO: Limitar que T sea int o float
def safe_reciprocal(t: T) -> Option[T]:
    return Option(1 / t) if t != 0 else Option(None)


# Ejercicio 3
# Safe root y safe reciprocal composition
def safe_root(t: T) -> Option[T]:
    return Option(sqrt(t)) if t >= 0 else Option(None)


safe_root_reciprocal = optional_composition(safe_reciprocal,
                                            safe_root)
