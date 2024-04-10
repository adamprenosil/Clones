

from folpy.semantics import Model
from folpy.syntax.types import Type
from folpy.semantics.lattices import Lattice, poset_to_lattice
from folpy.semantics.modelfunctions import Operation_decorator, Relation_decorator

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

def gen_meet_irr_lattice(lattice):
    """
    >>> from folpy.examples.posets import M3, gen_chain
    >>> A = M3 * gen_chain(2)
    >>> gen_meet_irr_lattice(poset_to_lattice(A)).universe
    [(2, 1), (0, 0), (3, 1), (1, 1), (1, 0), (4, 1)]
    """
    universe = set(lattice.meet_irreducibles())
    universe.add(lattice.min())
    universe.add(lattice.max())
    universe = list(universe)

    return gen_lattice_from_set(universe, lattice)
    
def gen_join_irr_lattice(lattice):
    universe = set(lattice.join_irreducibles())
    universe.add(lattice.min())
    universe.add(lattice.max())
    universe = list(universe)

    return gen_lattice_from_set(universe, lattice)

def gen_meet_irr_and_join_irr_lattice(lattice):
    universe = set(lattice.meet_irreducibles()).union(set(lattice.join_irreducibles()))
    universe.add(lattice.min())
    universe.add(lattice.max())
    universe = list(universe)

    return gen_lattice_from_set(universe, lattice)

def gen_lattice_from_set(universe, lattice):

    @Relation_decorator(universe)
    def le(x,y):
        return lattice.le(x,y)
    
    poset = Model(
        Type({}, {"<=": 2}),
        universe,
        {},
        {'<=': le}
    )
    
    return poset_to_lattice(poset)