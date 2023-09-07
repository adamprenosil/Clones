
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
        assert pairs != None or type(matrix) != type(None), "la relación hay que cargarla por la lista de pares o la matriz"
        self.pairs = pairs
        if type(matrix) != type(None):
            self.matrix = matrix
        elif isinstance(pairs, list):
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
            result += indent(repr(self.matrix))
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
        if (self.matrix != other.matrix).any():
            return False
        return True
    
    def __ne__(self, other):
        """
        Triste necesidad para la antiintuitiva logica de python
        'A==B no implica !(A!=B)'
        """
        return not self.__eq__(other)
    
    def __lt__(self, other):
        """
        La relación de orden dada por orden lexicográfico
        """
        for self_row, other_row in zip(self.matrix, other.matrix):
            for self_elem, other_elem in zip(self_row, other_row):
                if self_elem < other_elem:
                    return True
                elif self_elem > other_elem:
                    return False
        return False
    
    def __le__(self, other):
        return self < other or self == other
    
    def __gt__(self, other):
        return other < self
    
    def __ge__(self, other):
        return self > other or self == other

    def __mul__(self, other):
        """
        La relacion resultante de intersecar self con other
        """
        return self.intersection(other)

    def __matmul__(self, other):
        """
        La relacion resultante de componer self con other
        """
        return self.compose(other)

    def __and__(self, other):
        """
        La relacion resultante de intersecar self con other
        """
        return self.intersection(other)

    def T(self):
        """
        La relacion transpuesta (i.e. (a,b) in B.T() si y solo si (b,a) in B)
        """
        return BinaryRelation(self.universe, matrix=self.matrix.T)
    
    def repr_by_T(self):
        """
        Devuelve la relación binaria representante entre `self` y su transpuesta
        Es la menor entre las 2
        """
        t = self.T()
        if t < self:
            return t
        return self

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
    
    def to_list(self):
        """
        Para convertir la relación a una lista, y poder guardarla en el disco
        con json. Guarda la información de la matriz, con la función to_list
        de numpy
        """
        return self.matrix.tolist()
    
    def list_of_pairs(self):
        """
        Genera la lista de pares a partir de la matriz
        """
        if self.pairs:
            return self.pairs
        else:
            pairs = numpy.argwhere(self.matrix).tolist()
            pairs = [tuple(x) for x in pairs]
            self.pairs = pairs
            return pairs

def top_relation(universe):
    pairs = [(a,b) for a in universe for b in universe]
    return BinaryRelation(universe, pairs=pairs)

def bottom_relation(universe):
    pairs = [(a,a) for a in universe]
    return BinaryRelation(universe, pairs=pairs)

def empty_relation(universe):
    pairs = []
    return BinaryRelation(universe, pairs=pairs)
