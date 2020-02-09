from typing import TypeVar, Callable, List

'''
EXAMPLE 1 - Composition
-----------------------

Haskell code:

f :: A -> B
g :: B -> C
h :: C -> D

composition = g . f


La compositión es asociativa

(h . g) . f = h . (g . f) = h . g . f

'''

A = TypeVar('A')
B = TypeVar('B')
C = TypeVar('C')
D = TypeVar('D')


def f(a: A) -> B:
    return len(a)


def g(b: B) -> C:
    return 2.1 * b


def h(c: C) -> D:
    return List[c]


def compose(g: Callable[[A], B],
            f: Callable[[B], C]) -> Callable[[A], C]:

    def inner(arg: A) -> C:
        print(arg)
        return g(f(arg))

    return inner

l: Callable[[A], C] = compose(g, f)
print(f"{l('Ejemplo 1')} es aprox 18.9")
m = compose(l, h)
m('Ejemplo 1')

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
