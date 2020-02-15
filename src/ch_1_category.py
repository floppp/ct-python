from typing import TypeVar, Callable, List

'''
EXAMPLE 1 - Composition
-----------------------

Haskell code:

f :: A -> B
g :: B -> C
h :: C -> D

composition = g . f


Composition is associative.

(h . g) . f = h . (g . f) = h . g . f

'''

A = TypeVar('A')
B = TypeVar('B')
C = TypeVar('C')
D = TypeVar('D')


def f(x: A) -> B:
    # return len(a)
    pass


def g(b: B) -> C:
    pass
#   return 2.1 * b


def h(c: C) -> D:
    pass
#   return List[c]


def compose(a: Callable[[B], C],
            b: Callable[[A], B]) -> Callable[[A], C]:

    def inner(arg: A) -> C:
        return a(b(arg))

    return inner


def comp(a: Callable[[B], C],
         b: Callable[[A], B]) -> Callable[[A], C]:
    return lambda arg: a(b(arg))


# h . (g . f)
l1 = compose(g, f)
m1 = compose(h, l1)

# (h . g) . f
l2 = compose(h, g)
m2 = compose(l2, f)


def f_impl(x: str) -> int:
    return int(x)


def g_impl(x: int) -> float:
    return x * 1.0


def h_impl(x: float) -> list:
    return [x]


'''
EXAMPLE 2 - identity
--------------------

Haskell code:

id :: A -> a
id x = x

Scala code:

def identity[A](a: A): A = a

'''


def identity(a: A) -> A:
    return a


id_lambda: Callable[[A], A] = lambda a: a


'''
EXAMPLE 3 - identity composition
--------------------

Haskell code:

f . id == f
id . f == f

Scala code:

f compose identity[A]   == f
identity[B] _ compose f == f

'''
# In test file.
