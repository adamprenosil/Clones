
from folpy.semantics.lattices import Lattice
from folpy.semantics.modelfunctions import Operation_decorator

def gen_coclon_lattice(coclones):
    """
    Genera el modelo de reticulado a partir de la lista de los coclones como
    conjuntos.
    """
    universe = range(len(coclones))

    @Operation_decorator(universe)
    def meet(c1,c2):
        return coclones.index(coclones[c1].intersection(coclones[c2]))
    
    @Operation_decorator(universe)
    def join(c1,c2):
        union = coclones[c1].union(coclones[c2])
        up_union = [x for x in coclones if union.issubset(x)]
        result = min(up_union)
        return coclones.index(result)

    return Lattice(universe, join, meet)
