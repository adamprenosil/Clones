import logging
from itertools import product

from coclon_utils import gen_coclones

def operation_preserve_relation(operation, relation):
    """
    Función que decide si una operación preserva una relación.
    - La operación está dada por una matriz multidimensional donde cada dimensión
    es el elemento en el lugar i que se le pasa a la función, y cada elemento 
    de la matriz es el resultado de la función.
    - La relación está dada por una lista de tuplas.
    """
    for pairs in product(relation, repeat=function_arity):
        pass
    return True

def find_operation(rels_preserved, rels_not):
    """
    función que dado 2 conjuntos de relaciones A y B, encuentra una operacion f 
    que preserva las relaciones de A y no preserva las relaciones de B
    - En el conjunto A alcanza con las relaciones generadoras de lozetas
    - En el conjunto B alcanza con pasar las relaciones minimales que queremos que
    no preserve
    """
    return True


def gen_clones(algebra, coclones_and_generators=None):
    universe = algebra.universe
    assert universe == list(range(len(universe)))

    if coclones_and_generators:
        assert len(coclones_and_generators) == 2
        (coclones, generators) = coclones_and_generators
    else:
        (coclones, generators) = gen_coclones(algebra)
    clones = []
    coclones_indexes = range(len(coclones))
    for i in coclones_indexes:
        coclon = coclones[i]
        generator = generators[i]
        for arity in range(2):
            for fun_matrix in product(universe, repeat=arity):
                # pasar el vector a matriz antes que nada
                pass

    return clones