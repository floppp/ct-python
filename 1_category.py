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


# h . (g . f)
l1 = compose(g, f)
m1 = compose(h, l1)

# (h . g) . f
l2 = compose(h, g)
m2 = compose(l2, f)


def f_impl(x: str) -> int:
    return int(x)


def g_impl(x: int) -> float:
    return x * 2.1


def h_impl(x: float) -> list:
    return [x]

'''
if __name__ == '__main__':
    print('\nEjemplo 1')
    composition: Callable[[A], C] = compose(g, f)
    # assert h('Ejemplo 1') == 18.9
    print(f"{composition('Ejemplo 1')} es aprox 18.9")
    print('\nEjemplo 2')
    # l = compose(g, f)
    # m = compose(l, h)
    # print(f"h . (g . f) = {m('Ejemplo 2a')}")
    l = compose(h, g)
    m = compose(l, f)
#    print(f"(h . g) . f = {m}")

'''
