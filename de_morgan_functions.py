from folpy.semantics.algebras import Algebra
from folpy.syntax.types import AlgebraicType
from folpy.semantics.modelfunctions import Operation_decorator

# Creo el tipo del álgebra como un diccionario de 
# {"nombre de función" : aridad}
tipo = AlgebraicType({"t": 0, "wedge": 2, "neg": 1, "delta": 1})

# Universo del algebra
universe = list(range(5))

tt = 1
ff = 0
nn = 2
bb = 3

# Definición de las funciones usando el decorador
@Operation_decorator(universe)
def t():
    return tt
@Operation_decorator(universe)
def f():
    return ff
@Operation_decorator(universe)
def n():
    return nn
@Operation_decorator(universe)
def b():
    return bb
@Operation_decorator(universe)
def neg(x):
    if x == tt:
        return ff
    elif x == ff:
        return tt
    else:
        return x 
@Operation_decorator(universe)
def wedge(x,y):
    if x == tt:
        return y
    elif x == ff:
        return ff
    elif y == tt:
        return x
    elif y == ff:
        return x
    elif x == y:
        return x
    else:
        return ff
@Operation_decorator(universe)
def vee(x,y):
    return neg(wedge(neg(x),neg(y)))
@Operation_decorator(universe)
def delta(x):
    if x == tt or x == bb:
        return tt
    else:
        return ff
@Operation_decorator(universe)
def nabla(x):
    return neg(delta(neg(x)))
@Operation_decorator(universe)
def box(x):
    return wedge(delta(x),nabla(x))
@Operation_decorator(universe)
def diamond(x):
    return vee(delta(x),nabla(x))
@Operation_decorator(universe)
def confl(x):
    if x == nn:
        return bb
    elif x == bb:
        return nn
    else:
        return x
@Operation_decorator(universe)
def otimes(x,y):
    if x == bb:
        return y
    elif x == nn:
        return nn
    elif y == bb:
        return x
    elif y == nn:
        return x
    elif x == y:
        return x
    else:
        return nn
@Operation_decorator(universe)
def oplus(x,y):
    return confl(otimes(confl(x),confl(y)))
@Operation_decorator(universe)
def tbtob(x):
    if x == bb:
        return bb
    else:
        return tt
@Operation_decorator(universe)
def tnton(x):
    if x == nn:
        return nn
    else:
        return tt
@Operation_decorator(universe)
def idbton(x):
    if x == bb:
        return nn
    else:
        return x
@Operation_decorator(universe)
def idntob(x):
    if x == nn:
        return bb
    else:
        return x
@Operation_decorator(universe)
def pbpbin1(x,y):
    if y == ff:
        return ff
    elif y == bb:
        return bb
    elif y == tt and x != bb:
        return tt
    elif y == tt and x == bb:
        return bb
    elif y == nn and x != nn:
        return ff
    elif y == nn and x == nn:
        return nn
@Operation_decorator(universe)
def pbpbin2(x,y):
    if y == ff:
        return ff
    elif y == nn:
        return nn
    elif y == tt and x != nn:
        return tt
    elif y == tt and x == nn:
        return nn
    elif y == bb and x != bb:
        return ff
    elif y == bb and x == bb:
        return bb
@Operation_decorator(universe)
def disc(x,y,z):
    if x == y:
        return z
    else:
        return x

# Creamos el álgebra con el tipo, el universo y la interpretación de cada 
# función
alg = Algebra(
    tipo, 
    universe, 
    {"t": t, "wedge": wedge, "neg": neg, "delta": delta}
)

# Guardamos el álgebra a memoria en la carpeta `Models/` y con el nombre 
# `exampleAlgebra.model` en este caso
alg.to_file("Models/exampleAlgebra.model")
