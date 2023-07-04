
from itertools import product

from binary_relation import bottom_relation,top_relation

def one_rel_closure(rel):
    """
    Obtiene el conjunto de relaciones binarias que es la clausura de `rel` con 
    las operaciones T, @ y *
    """
    universe = rel.universe
    initial_set = {bottom_relation(universe), 
                   top_relation(universe)}

    return closure_of_union(initial_set, {rel, rel.T()})


def closure_of_union(brs1, brs2):
    """
    Obtiene el conjunto de relaciones binarias que es la clausura de dos 
    dos conjuntos clausurados de relaciones `brs1` `brs2` con las
    operaciones T, @ y *
    """
    initial_set = brs1
    aux_set = brs2.difference(brs1)
    closure_set = brs1.copy()
    
    while aux_set:
        initial_set = initial_set.union(aux_set)
        for old_or_new_rel, new_rel in product(initial_set, aux_set):
            if old_or_new_rel != new_rel:
                closure_set.add(old_or_new_rel * new_rel)
                closure_set.add(old_or_new_rel @ new_rel)
                closure_set.add(new_rel @ old_or_new_rel)
            else:
                closure_set.add(old_or_new_rel @ new_rel)
        aux_set = closure_set.difference(initial_set)

    return closure_set

def generate_key_list(generator, tiles, previous_set=None):
    if type(previous_set) != list:
        previous_set = tiles.keys()
    result = [i for i in previous_set if i not in tiles[generator]]

    return result

def generate_coclones_by_antichains(tiles):
    generators = tiles.keys()
    two_br_generator = [i for i in generators if len(tiles[i]) == 2][0]
    two_br_generator_key_list = generate_key_list(two_br_generator, tiles)
    coclones = {two_br_generator_key_list: tiles[two_br_generator]}
    
    initial_set = coclones.copy()
    aux_set = tiles.copy().pop(two_br_generator)

    while aux_set:
        pass

    return coclones