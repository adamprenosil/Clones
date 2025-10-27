from folpy.semantics.algebras import Algebra
from folpy.syntax.types import AlgebraicType
from folpy.semantics.modelfunctions import Operation_decorator

# Creo el tipo del álgebra como un diccionario de 
# {"nombre de función" : aridad}
tipo = AlgebraicType({"top": 0, "bottom": 0, "d": 3, "f": 3})
#tipo = AlgebraicType({"top": 0, "bottom": 0, "d": 3})

# Universo del algebra
universe = list(range(5))

# Definición de las funciones usando el decorador
@Operation_decorator(universe)
def top():
    return 1
@Operation_decorator(universe)
def bottom():
    return 0
@Operation_decorator(universe)
def disc(x,y,z):
    if x == y:
        return z
    else:
        return x
@Operation_decorator(universe)
def f(x,y,z):
    if x == 2 and y == 3 and z == 4:
        return top()
    else:
        return bottom()

# Creamos el álgebra con el tipo, el universo y la interpretación de cada 
# función
alg = Algebra(
    tipo, 
    universe, 
    {"top": top, "bottom": bottom, "d": disc, "f": f}
)

# Guardamos el álgebra a memoria en la carpeta `Models/` y con el nombre 
# `exampleAlgebra.model` en este caso
alg.to_file("Models/exampleAlgebra.model")
