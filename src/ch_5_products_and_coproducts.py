from typing import TypeVar, Tuple

'''
Morfismos <- Relaciones entre objectos

Es obvio a partir de flechas entre objetos, pero viene bien ponerlo en palabras.
'''

'''
El objeto inicial es el objeto inicial es aqué que tiene un y solo un
morfismo iendo a culquier otro objeto de la categoría.

Esto no garantiza que sea único. Pero sí que dos objetos iniciales
cualesquiera son isomórficos.
'''

# absurd :: Void -> a

# def absurd[A]: Nothing => A

'''
Por contra, el objeto terminal es el objeto con uno y solo un morfismo
hacia él desde cualquier objeto de la categoría.

Al igual que el objeto inicial, dos terminales cualesquiera son
isomórficos.
'''

'''
Inicial -> Any en scala
Final   -> Nothing en scala
'''
# unit :: a -> ()
# unit _ = ()

# def unit[A]: A => Unit = _ => ()

'''
DUALIDAD

La única diferencia entre el objeto inicial y el final es la dirección
del morfismo. Resulta que de cualquier categoría C podemos definir su
categoría opuesta C_op, simplemente cambiando el sentido de las flechas.

Este concepto de dualidad nos da que, a partir de cualquier estructura,
tenemos la opuesta:
 - mónada <-> comónada
 - producto <-> coproructo
 - ...

Así, un objeto terminal es el inicial en la categoría opuesta, y viceversa.
'''

'''
ISOMORFISMO

Isomorphic objects look the same —they have the same shape. It means that
every part of one object corresponds to some part of another object in a
one-to-one mapping. Mathematically it means that there is a mapping from
object 𝑎 to object 𝑏, and there is a mapping from object 𝑏 back to
object 𝑎, and they are the inverse of each other.
In category theory we replace mappings with morphisms. An isomorphism is
an invertible morphism; or a pair of morphisms, one being the inverse
of the other.
'''

# f . g = id
# g . f = id

# f compose g == identity _
# g compose f == identity _

'''
PRODUCTO

'''

# fst :: (a,b) -> a
# fst (x,y) = x

# def fst[A, B]: ((A, B)) => A = { case (x, y) => x }

# snd :: (a,b) -> b
# snd (x,y) = y

# def snd[A, B]: ((A, B)) => B = { case (x, y) => y }

# fst (x, _) = x
# snd (_,y) = y

# def fst[A, B]: ((A, B)) => A = _._1
# def snd[A, B]: ((A, B)) => B = _._2

A = TypeVar('A')
B = TypeVar('B')


def first(p: Tuple[A, B]) -> A: return p[0]
