
import numpy
from itertools import chain
from folpy.utils import indent


class BinaryRelation(object):

    """
    Abstracción para trabajar con relaciones binarias, representadas como 
    matrices de transiciones.
    """

    def __init__(self, universe, pairs=None, matrix=None, name=""):
        assert not isinstance(universe, int)
        assert isinstance(universe, list), "El universo debe ser una lista"
        self.universe = sorted(universe)
        self.universe_card = len(self.universe)
        assert pairs or matrix, "la relación hay que cargarla por la lista de pares o la matriz"
        if matrix:
            self.matrix = matrix
        elif pairs:
            assert isinstance(pairs, list), "La relación se debe pasar como una lista de pares"
            assert all(isinstance(x, tuple) or len(x)==2 for x in pairs), "La relación se debe pasar como una lista de pares"
            self.matrix = numpy.zeros((self.universe_card, self.universe_card), 
                                      dtype=bool)
            for (i,j) in pairs:
                self.matrix[i,j] = True
        self.name = name
        self.class_name = type(self).__name__

    def __repr__(self):
        if self.name:
            return "%s(name= %s)\n" % (self.class_name, self.name)
        else:
            result = self.class_name + "(\n"
            result += indent(repr(self.universe) + ",\n")
            result += indent(repr(self.matrix) + ",\n")
            return result + ")"

    def __hash__(self):
        """
        Hash para las relaciones binarias
        """
        return hash(frozenset(chain(self.universe,
                                    str(self.matrix))))
    
    def __eq__(self, other):
        if self.universe != other.universe:
            return False
        if self.matrix != other.matrix:
            return False
        return True
    
    def __ne__(self, other):
        """
        Triste necesidad para la antiintuitiva logica de python
        'A==B no implica !(A!=B)'
        """
        return not self.__eq__(other)

    def __mul__(self, other):
        """
        La relacion resultante de intersecar self con other
        """
        return self.intersection(self, other)

    def __matmul__(self, other):
        """
        La relacion resultante de componer self con other
        """
        return self.compose(self, other)

    def __and__(self, other):
        """
        La relacion resultante de intersecar self con other
        """
        return self.intersection(self, other)

    def T(self):
        """
        La relacion transpuesta (i.e. (a,b) in B.T() si y solo si (b,a) in B)
        """
        return BinaryRelation(self.universe, matrix=self.matrix.T)

    def intersection(self, other):
        """
        La relacion resultante de intersecar self con other
        """
        matrix = self.matrix * other.matrix
        return BinaryRelation(self.universe, matrix=matrix)

    def compose(self, other):
        """
        La relacion resultante de componer self con other
        """
        matrix = self.matrix @ other.matrix
        return BinaryRelation(self.universe, matrix=matrix)


def top_relation(universe):
    pairs = [(a,b) for a in universe for b in universe]
    return BinaryRelation(universe, pairs=pairs)

def bottom_relation(universe):
    pairs = [(a,a) for a in universe]
    return BinaryRelation(universe, pairs=pairs)

# def rel_clousure(rel):
#     """
#     Obtiene el conjunto de relaciones binarias que es la clausura de `rel` con 
#     las operaciones T, @ y *
#     """
#     universe = rel.universe
#     clausure_set = {bottom_relation(universe), top_relation(universe), rel}
#     new_rels = clausure_set.copy()
#     new_new_rels = set()

#     while(new_rels != set()):
#         for old_rel in clausure_set:
#             for new_rel in new_rels:
#                 intersection = old_rel * new_rel
#                 composition = old_rel @ new_rel
#                 new_new_rels.add(intersection)
#                 new_new_rels.add(composition)


#     return clausure_set