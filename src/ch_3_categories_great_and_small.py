from typing import Callable, TypeVar, Generic
from functools import singledispatch
from abc import ABCMeta
from abc import abstractmethod

''' MONOID

Definicion
----------
Estructura con dos funciones, una que devuelve el valor que contiene, otra
que concatena los valores de dos de dichas estructuras.
----------

class Monoid m where
    mempty :: m
    mappend :: m -> m -> m

trait Monoid[M] {
    def combine(m1: M, m2: M): M
    def empty: M
}
'''

M = TypeVar('M')


class Monoid(Generic[M], metaclass=ABCMeta):

    @abstractmethod
    def empty(self) -> M:
        ...

    @abstractmethod
    def combine(self, m1: M, m2: M) -> M:
        ...

# Podemos definirlo también con @singledispatch


@singledispatch
def sd_empty(a: M) -> M:
    raise NotImplementedError


@singledispatch
def sd_combine(a: M, b: M) -> M:
    raise NotImplementedError


''' STRING MONOID
instance Monoid String where
    mempty = ""
    mappend = (++)

object Monoid {
    implicit val stringMonoid: Monoid[String] = new Monoid[String] {
        def combine(m1: String, m2: String): String = m1 + m2
        def empty: String = ""
    }
}
'''


class String(Monoid[str]):

    def empty(self) -> str:
        return ''

    def combine(self, m1: str, m2: str) -> str:
        return m1 + m2


# Podemos hace lo mismo con singledispatch.
@sd_empty.register(str)
def _(a: str) -> str:
    return ''


@sd_combine.register(str)
def _(a: str, b: str) -> str:
    return a + b


@sd_empty.register(list)
def _(a: list) -> list:
    return []


@sd_combine.register(list)
def _(a: list, b: list) -> list:
    return a + b
