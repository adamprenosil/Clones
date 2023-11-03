import logging
from itertools import product, repeat
import numpy as np
import datetime
from multiprocessing import Pool
from collections import defaultdict

from coclon_utils import gen_coclones

def arreq_in_list(myarr, list_arrays):
    return next((True for elem in list_arrays if np.array_equal(elem, myarr)), False)


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

def process_fun_matrix(fun_matrix_tuple, n, arity, subuniverses, gen_codes):
    fun_matrix = np.array(fun_matrix_tuple).reshape(tuple(n for _ in range(arity)))
    code = [op_preserve_relation(fun_matrix, sub.list_of_pairs()) for sub in subuniverses]
    if code in gen_codes.values():
        return (list(gen_codes.values()).index(code), fun_matrix)

def gen_clones(algebra, coclones_and_generators=None):
    universe = algebra.universe
    assert universe == list(range(len(universe)))
    n = len(universe)
    
    if coclones_and_generators:
        assert len(coclones_and_generators) == 2
        (coclones, generators) = coclones_and_generators
    else:
        (coclones, generators) = gen_coclones(algebra)

    clones = defaultdict(list)
    gen_codes = {}
    coclones_indexes = range(len(coclones))
    subuniverses = list(set.union(*[set(g) for g in generators]))
    for i in coclones_indexes:
        code = [sub in coclones[i] for sub in subuniverses]
        gen_codes[i] = code
        clones[i] = []
    
    for arity in range(1,3):
        logging.info("Empiezo aridad %s" % arity)
        contador = 0
        pool = Pool(4)
        for k, v in pool.starmap(process_fun_matrix, zip(
            product(universe, repeat=n**arity),
            repeat(n),
            repeat(arity),
            repeat(subuniverses),
            repeat(gen_codes),

        )):
            contador += 1
            if contador % 100000 == 0:
                logging.info("cantidad %s: %s" % (contador, datetime.datetime.now()))
            clones[k].append(v)
        pool.close()
        logging.info("toy aca")
        pool.join()
    return clones

