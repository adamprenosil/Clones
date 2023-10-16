import logging
from itertools import product
import numpy as np

from coclon_utils import gen_coclones

def op_preserve_relations(operation, relations):
    """
    Función que decide si una operación preserva un conjunto de relaciones.
    - La operación está dada por una matriz multidimensional donde cada dimensión
    es el elemento en el lugar i que se le pasa a la función, y cada elemento 
    de la matriz es el resultado de la función.
    - Las relaciones están dadas por una lista de lista de tuplas.
    """
    for rel in relations:
        op_preserve_rel = op_preserve_relation(operation, rel)
        if not op_preserve_rel:
            return False
    return True

def op_preserve_relation(operation, relation):
    """
    Función que decide si una operación preserva una relación.
    - La operación está dada por una matriz multidimensional donde cada dimensión
    es el elemento en el lugar i que se le pasa a la función, y cada elemento 
    de la matriz es el resultado de la función.
    - La relación está dada por una lista de tuplas.
    """
    arity = len(operation.shape)
    for t in product(relation, repeat=arity):
        tuple_after_op = (operation[tuple(t[i][0] for i in range(arity))],
                          operation[tuple(t[i][1] for i in range(arity))])
        preserve_tuple = tuple_after_op in relation
        if not preserve_tuple:
            return False
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
    n = len(universe)

    if coclones_and_generators:
        assert len(coclones_and_generators) == 2
        (coclones, generators) = coclones_and_generators
    else:
        (coclones, generators) = gen_coclones(algebra)
    clones = [[] for _ in range(len(coclones))]
    clones_finished = [False for _ in range(len(coclones))]
    all_binrels = set.union(*coclones)
    coclones_indexes = range(len(coclones))
    for i in coclones_indexes:
        print("clon %s de %s" % (i, len(coclones)))
        coclon = coclones[i]
        binrels_complement = all_binrels - coclon
        generators_i = [g.list_of_pairs() for g in generators[i]]
        for arity in range(1,3):
            for fun_matrix_tuple in product(universe, repeat=n**arity):
                fun_matrix = np.array(fun_matrix_tuple).reshape(tuple(n for _ in range(arity)))
                preserve_gens = op_preserve_relations(fun_matrix, generators_i)
                if not preserve_gens:
                    continue
                clones[i].append(fun_matrix)
                not_preserving_rels = set() 
                for rel in binrels_complement:
                    preserve = op_preserve_relation(fun_matrix, rel.list_of_pairs())
                    if not preserve:
                        not_preserving_rels.add(rel)
                
                binrels_complement = binrels_complement - not_preserving_rels
                if not binrels_complement:
                    clones_finished[i] = True
                    break
    
    print(clones_finished)
    return clones