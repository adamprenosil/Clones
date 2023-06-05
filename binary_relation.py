
import numpy
from folpy.utils import indent


class BinaryRelation(object):

    """
    Abstracción para trabajar con relaciones binarias, representadas como 
    matrices de transiciones.
    """

    def __init__(self, universe, pairs, name=""):
        assert not isinstance(universe, int)
        assert isinstance(universe, list), "El universo debe ser una lista"
        assert isinstance(pairs, list), "La relación se debe pasar como una lista de pares"
        assert all(isinstance(x, tuple) for x in pairs), "La relación se debe pasar como una lista de pares"
        self.universe = sorted(universe)
        self.pairs = sorted(pairs)
        self.universe_card = len(self.universe)
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
