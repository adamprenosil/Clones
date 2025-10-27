from folpy.semantics.algebras import Algebra
from folpy.syntax.types import AlgebraicType
from folpy.semantics.modelfunctions import Operation_decorator

# Creo el tipo del álgebra como un diccionario de 
# {"nombre de función" : aridad}
typeDMA = AlgebraicType({"t": 0, "wedge": 2, "neg": 1})
typeN = AlgebraicType({"t": 0, "wedge": 2, "neg": 1, "n": 0})
typeB = AlgebraicType({"t": 0, "wedge": 2, "neg": 1, "b": 0})

# Clones preserving subalgebras

typeDelta = AlgebraicType({"t": 0, "wedge": 2, "neg": 1, "delta": 1})
typeB2K3P3 = typeDelta
typeDeltaN = AlgebraicType({"t": 0, "wedge": 2, "neg": 1, "delta": 1, "n": 0})
typeK3 = typeDeltaN
# typeDeltaN = typeBoxN
typeDeltaB = AlgebraicType({"t": 0, "wedge": 2, "neg": 1, "delta": 1, "b": 0})
typeP3 = typeDeltaB
# typeDeltaB = typeBoxB
typeB2K3 = AlgebraicType({"t": 0, "wedge": 2, "neg": 1, "delta": 1, "idbton": 1})
typeDeltaIdbton = typeB2K3
typeB2P3 = AlgebraicType({"t": 0, "wedge": 2, "neg": 1, "delta": 1, "idntob": 1})
typeDeltaIdntob = typeB2P3

# Persistent clones

typePersistent = AlgebraicType({"t": 0, "wedge": 2, "neg": 1, "oplus": 2, "otimes": 2})
typeOplusOtimes = typePersistent
typePersistentB2 = AlgebraicType({"t": 0, "wedge": 2, "neg": 1, "pbpbin1": 2, "pbpbin2": 2})
typePersistentK3 = AlgebraicType({"t": 0, "wedge": 2, "neg": 1, "pbpbin1": 2, "pbpbin2": 2, "n": 0})
typePersistentP3 = AlgebraicType({"t": 0, "wedge": 2, "neg": 1, "pbpbin1": 2, "pbpbin2": 2, "b": 0})

# Discriminator clones

typeBox = AlgebraicType({"t": 0, "wedge": 2, "neg": 1, "box": 1})
typeConfl = AlgebraicType({"t": 0, "wedge": 2, "neg": 1, "confl": 1})
typeBoxDeltanb = AlgebraicType({"t": 0, "wedge": 2, "neg": 1, "deltanb": 2})
# typeDelta
# typeDeltaIdbton
# typeDeltaIdntob
# typeDeltaN
# typeDeltaB
typeDeltaConfl = AlgebraicType({"t": 0, "wedge": 2, "neg": 1, "delta": 1, "confl": 1})

# minimal protoalgebraic clones

typeEquivtmin = AlgebraicType({"t": 0, "wedge": 2, "neg": 1, "equivtmin": 2})
typeEquivimin = AlgebraicType({"t": 0, "wedge": 2, "neg": 1, "equivimin": 2})

# other

typeTnton = AlgebraicType({"t": 0, "wedge": 2, "neg": 1, "tnton": 1})
typeTbtob = AlgebraicType({"t": 0, "wedge": 2, "neg": 1, "tbtob": 1})
typeIdntob = AlgebraicType({"t": 0, "wedge": 2, "neg": 1, "idntob": 1})
typeIdbton = AlgebraicType({"t": 0, "wedge": 2, "neg": 1, "idbton": 1})
typeOplus = AlgebraicType({"t": 0, "wedge": 2, "neg": 1, "oplus": 2})
typeOtimes = AlgebraicType({"t": 0, "wedge": 2, "neg": 1, "otimes": 2})
typeMnhbin1 = AlgebraicType({"t": 0, "wedge": 2, "neg": 1, "mnhbin1": 2})
typeMnhbin2 = AlgebraicType({"t": 0, "wedge": 2, "neg": 1, "mnhbin2": 2})
typeNhbin1 = AlgebraicType({"t": 0, "wedge": 2, "neg": 1, "nhbin1": 2})
typeNhbin2 = AlgebraicType({"t": 0, "wedge": 2, "neg": 1, "nhbin2": 2})


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
def deltanb(x,y):
    if x == nn and y == bb:
        return tt
    else:
        return ff
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
def mnhbin1(x,y):
    if x == nn and y == bb:
        return ff
    elif x == tt:
        return ff
    else:
        return y
@Operation_decorator(universe)
def mnhbin2(x,y):
    if x == bb and y == nn:
        return ff
    elif y == tt:
        return ff
    else:
        return y
@Operation_decorator(universe)
def nhbin1(x,y):
    if x == bb and y == nn:
        return nn
    else:
        return ff
@Operation_decorator(universe)
def nhbin2(x,y):
    if x == nn and y == nn:
        return nn
    if x == bb and y == nn:
        return nn
    if x == bb and y == bb:
        return bb
    else:
        return ff
@Operation_decorator(universe)
def nhbin3(x,y):
    if x == nn and y == bb:
        return bb
    else:
        return ff
@Operation_decorator(universe)
def nhbin4(x,y):
    if x == nn and y == nn:
        return nn
    elif x == nn and y == bb:
        return bb
    elif x == bb and y == bb:
        return bb
    else:
        return ff
@Operation_decorator(universe)
def mhnpbin(x,y):
    if x == tt or x == ff:
        return tt
    elif x == nn and y == bb:
        return ff
    elif x == bb and y == nn:
        return ff
    else:
        return x
@Operation_decorator(universe)
def mnpbin1(x,y):
    if x == bb and y == nn:
        return ff
    elif x == nn and y == bb:
        return ff
    elif y == bb:
        return bb
    else:
        return vee(x,neg(x))
@Operation_decorator(universe)
def mnpbin2(x,y):
    if x == bb and y == nn:
        return ff
    else:
        return vee(x,neg(x))
@Operation_decorator(universe)
def mnpbin3(x,y):
    if x == nn and y == bb:
        return ff
    elif x == bb and y == nn:
        return ff
    elif y == nn:
        return nn
    else:
        return vee(x,neg(x))
@Operation_decorator(universe)
def mnpbin4(x,y):
    if x == nn and y == bb:
        return ff
    else:
        return vee(x,neg(x))
@Operation_decorator(universe)
def npbin1(x,y):
    if x == tt and y == nn:
        return nn
    elif x == tt and y == bb:
        return bb
    else:
        return ff
@Operation_decorator(universe)
def npbin2(x,y):
    if x == tt and y == nn:
        return nn
    elif x == tt and y == bb:
        return bb
    elif x == bb and y == bb:
        return bb
    else:
        return ff
@Operation_decorator(universe)
def npbin3(x,y):
    if x == tt and y == nn:
        return nn
    else:
        return ff
@Operation_decorator(universe)
def mhnpteraux(x,y):
    if x == tt:
        return bb
    elif x == ff:
        return ff
    elif x == nn:
        return ff
    elif x == bb and y == nn:
        return ff
    else:
        return bb
@Operation_decorator(universe)
def mhnpter(x,y,z):
    if y == tt:
        return ff
    elif y == ff:
        return ff
    elif x == nn and y == nn and z == bb:
        return ff
    elif x == tt and y == nn:
        return nn
    elif x == ff and y == nn:
        return ff
    elif x == bb and y == nn:
        return ff
    elif x == nn and y == nn:
        return nn
    else:
        return mhnpteraux(x,z)
@Operation_decorator(universe)
def mnpter1(x,y,z):
    if x == bb and y == bb and z == nn:
        return bb
    else:
        return mhnpter(x,y,z)
@Operation_decorator(universe)
def mnpter2(x,y,z):
    if x == tt and y == bb and z == nn:
        return ff
    else:
        return mhnpter(x,y,z)
@Operation_decorator(universe)
def npter1(x,y,z):
    if x == bb and y == bb and (z == tt or z == ff):
        return ff
    elif x == tt and y == bb and z != bb:
        return ff
    else:
        return mhnpter(x,y,z)
@Operation_decorator(universe)
def npter2(x,y,z):
    if y == bb:
        return ff
    else:
        return mhnpter(x,y,z)
@Operation_decorator(universe)
def imptmax(x,y):
    if (x == tt or x == bb) and (y == ff or y == nn):
        return nn
    else:
        return tt
@Operation_decorator(universe)
def impimax(x,y):
    if (x == tt or x == bb) and (y == ff or y == nn):
        return ff
    else:
        return bb
@Operation_decorator(universe)
def equivtmin(x,y):
    if x == y:
        return bb
    else:
        return ff
@Operation_decorator(universe)
def equivimin(x,y):
    if x == y:
        return tt
    else:
        return nn
@Operation_decorator(universe)
def disc(x,y,z):
    if x == y:
        return z
    else:
        return x

# Creamos el álgebra con el tipo, el universo y la interpretación de cada 
# función
algDMA = Algebra(
    typeDMA, 
    universe, 
    {"t": t, "wedge": wedge, "neg": neg}
)
algN = Algebra(
    typeN, 
    universe, 
    {"t": t, "wedge": wedge, "neg": neg, "n": n}
)
algB = Algebra(
    typeB, 
    universe, 
    {"t": t, "wedge": wedge, "neg": neg, "b": b}
)
algDelta = Algebra(
    typeDelta, 
    universe, 
    {"t": t, "wedge": wedge, "neg": neg, "delta": delta}
)
algDeltaN = Algebra(
    typeDeltaN, 
    universe, 
    {"t": t, "wedge": wedge, "neg": neg, "delta": delta, "n": n}
)
algDeltaB = Algebra(
    typeDeltaB, 
    universe, 
    {"t": t, "wedge": wedge, "neg": neg, "delta": delta, "b": b}
)
algDeltaIdbton = Algebra(
    typeDeltaIdbton, 
    universe, 
    {"t": t, "wedge": wedge, "neg": neg, "delta": delta, "idbton": idbton}
)
algDeltaIdntob = Algebra(
    typeDeltaIdntob, 
    universe, 
    {"t": t, "wedge": wedge, "neg": neg, "delta": delta, "idntob": idntob}
)
algOplusOtimes = Algebra(
    typeOplusOtimes, 
    universe, 
    {"t": t, "wedge": wedge, "neg": neg, "oplus": oplus, "otimes": otimes}
)
algPersistentB2 = Algebra(
    typePersistentB2, 
    universe, 
    {"t": t, "wedge": wedge, "neg": neg, "pbpbin1": pbpbin1, "pbpbin2": pbpbin2}
)
algPersistentK3 = Algebra(
    typePersistentK3, 
    universe, 
    {"t": t, "wedge": wedge, "neg": neg, "pbpbin1": pbpbin1, "pbpbin2": pbpbin2, "n": n}
)
algPersistentP3 = Algebra(
    typePersistentP3, 
    universe, 
    {"t": t, "wedge": wedge, "neg": neg, "pbpbin1": pbpbin1, "pbpbin2": pbpbin2, "b": b}
)
algBox = Algebra(
    typeBox, 
    universe, 
    {"t": t, "wedge": wedge, "neg": neg, "box": box}
)
algConfl = Algebra(
    typeConfl, 
    universe, 
    {"t": t, "wedge": wedge, "neg": neg, "confl": confl}
)
algBoxDeltanb = Algebra(
    typeBoxDeltanb, 
    universe, 
    {"t": t, "wedge": wedge, "neg": neg, "box": box, "deltanb": deltanb}
)
algDeltaConfl = Algebra(
    typeDeltaConfl, 
    universe, 
    {"t": t, "wedge": wedge, "neg": neg, "delta": delta, "confl": confl}
)
algEquivtmin = Algebra(
    typeEquivtmin, 
    universe, 
    {"t": t, "wedge": wedge, "neg": neg, "equivtmin": equivtmin}
)
algEquivimin = Algebra(
    typeEquivimin, 
    universe, 
    {"t": t, "wedge": wedge, "neg": neg, "equivimin": equivimin}
)
algTnton = Algebra(
    typeTnton, 
    universe, 
    {"t": t, "wedge": wedge, "neg": neg, "tnton": tnton}
)
algTbtob = Algebra(
    typeTbtob, 
    universe, 
    {"t": t, "wedge": wedge, "neg": neg, "tbtob": tbtob}
)
algIdntob = Algebra(
    typeIdntob, 
    universe, 
    {"t": t, "wedge": wedge, "neg": neg, "idntob": idntob}
)
algIdbton = Algebra(
    typeIdbton, 
    universe, 
    {"t": t, "wedge": wedge, "neg": neg, "idbton": idbton}
)
algOplus = Algebra(
    typeOplus, 
    universe, 
    {"t": t, "wedge": wedge, "neg": neg, "oplus": oplus}
)
algOtimes = Algebra(
    typeOtimes, 
    universe, 
    {"t": t, "wedge": wedge, "neg": neg, "otimes": otimes}
)
algMnhbin1 = Algebra(
    typeMnhbin1, 
    universe, 
    {"t": t, "wedge": wedge, "neg": neg, "mnhbin1": mnhbin1}
)
algMnhbin2 = Algebra(
    typeMnhbin2, 
    universe, 
    {"t": t, "wedge": wedge, "neg": neg, "mnhbin2": mnhbin2}
)
algNhbin1 = Algebra(
    typeNhbin1, 
    universe, 
    {"t": t, "wedge": wedge, "neg": neg, "nhbin1": nhbin1}
)
algNhbin2 = Algebra(
    typeNhbin2, 
    universe, 
    {"t": t, "wedge": wedge, "neg": neg, "nhbin2": nhbin2}
)

# Guardamos el álgebra a memoria en la carpeta `Models/` y con el nombre 
# `exampleAlgebra.model` en este caso
algDMA.to_file("Models/DMA.model")
algN.to_file("Models/N.model")
algB.to_file("Models/B.model")
algDelta.to_file("Models/Delta.model")
algDeltaN.to_file("Models/DeltaN.model")
algDeltaB.to_file("Models/DeltaB.model")
algDeltaIdbton.to_file("Models/DeltaIdbton.model")
algDeltaIdntob.to_file("Models/DeltaIdntob.model")
algOplusOtimes.to_file("Models/OplusOtimes.model")
algPersistentB2.to_file("Models/PersistentB2.model")
algPersistentK3.to_file("Models/PersistentK3.model")
algPersistentP3.to_file("Models/PersistentP3.model")
algBox.to_file("Models/Box.model")
algConfl.to_file("Models/Confl.model")
algBoxDeltanb.to_file("Models/BoxDeltanb.model")
algDeltaConfl.to_file("Models/DeltaConfl.model")
algEquivtmin.to_file("Models/Equivtmin.model")
algEquivimin.to_file("Models/Equivimin.model")
algTnton.to_file("Models/Tnton.model")
algTbtob.to_file("Models/Tbtob.model")
algIdntob.to_file("Models/Idntob.model")
algIdbton.to_file("Models/Idbton.model")
algOplus.to_file("Models/Oplus.model")
algOtimes.to_file("Models/Otimes.model")
algMnhbin1.to_file("Models/Mnhbin1.model")
algMnhbin2.to_file("Models/Mnhbin2.model")
algNhbin1.to_file("Models/Nhbin1.model")
algNhbin2.to_file("Models/Nhbin2.model")