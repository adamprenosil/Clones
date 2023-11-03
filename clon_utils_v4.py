import logging
from itertools import product, combinations
import numpy as np
import datetime
from collections import defaultdict

from coclon_utils import gen_coclones


class Node(object):

    def __init__(self, partial_func, code, last_pair) -> None:
        self.partial_func = partial_func
        self.code = code
        self.last_pair = last_pair
    
    def copy(self):
        from copy import deepcopy
        return deepcopy(self)


def next_pair(a, b, n):
    if b < n-1:
        return (a, b+1)
    elif b == n - 1 and a < n-1:
        return (a+1, 0)
    return (0, 0)  

def generate_preserv_table(relations, universe):
    n = len(universe)
    table = {}

    for ((a, b) , (c, d)) in combinations(product(universe, repeat=2), 2):
        for fab, fcd in product(universe, repeat=2):
            pair1, pair2 = (a, b, fab), (c, d, fcd)
            code = [True]*len(relations)
            for i in range(len(relations)):
                rel = relations[i]
                preserve = pair_preserve_relation(pair1, pair2, rel) and \
                            pair_preserve_relation(pair2, pair1, rel)
                code[i] = preserve
            table[(pair1, pair2)] = code

    return table

def pair_preserve_relation(pair1, pair2, relation):
    (a, b, fab), (c, d, fcd) = pair1, pair2
    if ((a,a) in relation) and ((b,b) in relation) and ((fab, fab) not in relation):
        return False
    if ((a,c) in relation) and ((b,d) in relation) and ((fab, fcd) not in relation):
        return False
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

    subuniverses = list(set.union(*[set(g) for g in generators]))
    relations = [sub.list_of_pairs() for sub in subuniverses]
    table = generate_preserv_table(relations, universe)

    clones = defaultdict(list)
    coclones_indexes = range(len(coclones))
    gen_codes = {}
    for i in coclones_indexes:
        code = [sub in coclones[i] for sub in subuniverses]
        gen_codes[i] = code
        clones[i] = []

    nodes_queue = []

    for x in range(n):
        code = [True]*len(relations)
        nodes_queue.append(Node([(0,0,x)], code, (0,0,x)))
    
    print(gen_codes)
    while nodes_queue:
        node = nodes_queue.pop(0)
        (a, b) = next_pair(node.last_pair[0],
                            node.last_pair[1],
                            n)
        for x in range(n):
            new_node = node.copy()
            new_pair = (a, b, x)
            for pair in new_node.partial_func:
                new_node.code = new_node.code and table[(pair, new_pair)]
            # if all(c == False for c in code):
            #     continue
            new_node.partial_func.append(new_pair)
            new_node.last_pair = new_pair
            if a == n-1 and b == n-1:
                print(new_node.code)
                if new_node.code in gen_codes.values():
                    clones[list(gen_codes.values()).index(new_node.code)].append(new_node.partial_func)
            else:
                nodes_queue.append(new_node)


    
    

    # for arity in range(1,3):
    #     contador = 0
    #     print(datetime.datetime.now())
    #     for fun_matrix_tuple in product(universe, repeat=n**arity):
    #         contador += 1
    #         if contador % 100000 == 0:
    #             print("cantidad %s: %s" % (contador, datetime.datetime.now()))
    #         fun_matrix = np.array(fun_matrix_tuple).reshape(tuple(n for _ in range(arity)))
    #         code = [op_preserve_relation(fun_matrix, sub.list_of_pairs()) for sub in subuniverses]
    #         if code in gen_codes.values():
    #             clones[list(gen_codes.values()).index(code)].append(fun_matrix)

    return clones

        

