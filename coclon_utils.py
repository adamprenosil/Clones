import logging
from itertools import product

from binary_relation import BinaryRelation, empty_relation, bottom_relation,top_relation


class Node(object):

    def __init__(self, closed, incomparables, generators) -> None:
        self.closed = closed
        self.incomparables = incomparables
        self.generators = generators
    
    def join(self, other):
        closed = closure_join(self.closed, other.closed)
        inc = [
            i for i in self.incomparables if 
            i in other.incomparables and i not in closed
            ]
        gen = self.generators + other.generators
        return Node(closed, inc, gen)

    def copy(self):
        from copy import deepcopy
        return deepcopy(self)

def to_file(coclones, path):
    """
    Guarda un diccionario de coclones con la estructura de 
        {generador: loseta}
    en la ruta `path` en formato json
    """
    assert path[-5:] == ".json"
    coclones_list_format = {}
    for key in coclones:
        key_list = key.tolist()
        coclon_set = [br.tolist() for br in coclones[key]]
        coclones_list_format[key_list] = coclon_set
    try:
        import json

        with open(path, 'w') as fp:
            json.dump(coclones_list_format, fp)
        return path
    except e:
        return e

def from_file(path):
    """
    Obtiene un diccionario de coclones con la estructura de 
        {generador: loseta}
    de la ruta `path` en formato json
    """
    assert path[-5:] == ".json"

    coclones = {}
    return coclones


def coclones_to_file(coclones, path):
    """"
    Guarda los coclones a un archivo con la siguiente estructura:
    Coclon 1
        Rel 1: [(par1), (par2)]
        Rel 2: ..
    Coclon 2
        ...
    """
    try:
        with open(path, 'w') as fp:
            i = 0
            for coclon in coclones:
                i += 1
                fp.write("Coclon %s \n" % i)
                j = 0
                for rel in coclon:
                    j += 1
                    fp.write("    Rel %s: %s \n" % (j, rel.list_of_pairs()))
        return path
    except e:
        return e


def one_rel_closure(rel):
    """
    Obtiene el conjunto de relaciones binarias que es la clausura de `rel` con 
    las operaciones T, @ y *
    """
    universe = rel.universe
    initial_set = {empty_relation(universe),
                   bottom_relation(universe), 
                   top_relation(universe)}

    return closure_join(initial_set, {rel, rel.T()})


def closure_join(brs1, brs2):
    """
    Obtiene el conjunto de relaciones binarias que es la clausura de dos 
    conjuntos clausurados de relaciones `brs1` `brs2` con las operaciones 
    T, @ y *
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


def generate_coclones_from_tiles_by_antichains(tiles):
    """
    Genera los coclones a partir de las losetas (generadores) y sus
    relaciones de inclusión. Utiliza un algoritmo de búsqueda por anticadenas.
    Retorna una lista de coclones y una lista de generadores.
    """
    logging.info("Generando coclones a partir de losetas")

    one_generators = list(tiles.keys())
    one_gen_nodes = {}
    nodes_queue = []

    while one_generators:
        g = one_generators.pop(0)
        incomparables = [
            x for x in one_generators if not (x in tiles[g] or g in tiles[x])
            ]
        node = Node(tiles[g], incomparables, [g])
        one_gen_nodes[g] = node
        nodes_queue.append(node.copy())
    
    coclones = []
    generators = []
    for g in tiles:
        coclones.append(tiles[g])
        generators.append([g])

    while nodes_queue:
        node = nodes_queue.pop(0)
        while node.incomparables:
            g = node.incomparables.pop(0)
            new_node = node.join(one_gen_nodes[g])
            if new_node.closed not in coclones:
                if new_node.incomparables:
                    nodes_queue.append(new_node)
                coclones.append(new_node.closed)
                generators.append(new_node.generators)
        print("termine incomparables del nodo, quedan %s" % len(nodes_queue))
        print("vamos %s gens y %s coclons" % (len(generators), len(coclones)))

    return (coclones, generators) 


def gen_coclones(algebra):
    """
    Genera los coclones de un álgebra a partir de sus relaciones binarias
    """

    algebra2 = algebra * algebra

    binary_relations = set()
    tiles = {} # diccionario de losetas (generador: loseta)

    i=0
    for sub in algebra2.subuniverses(proper=False):
        br = BinaryRelation(algebra.universe, pairs=sub)
        binary_relations.add(br)
        i += 1
        logging.info("%s : %s %s" % (i, sub, br))

        if br == br.repr_by_T():
            closure = one_rel_closure(br)
            if closure not in tiles.values():
                tiles[br] = closure
                logging.info("%s : %s" % (i, len(closure)))
        


    logging.info("%s : %s" % (
        "Cantidad de coclones 1-generados",
        len(tiles)
    ))

    (coclones, generators) = generate_coclones_from_tiles_by_antichains(tiles)

    logging.info("%s : %s" % (
        "Tamaños de coclones", [len(x) for x in coclones]
        ))
    logging.info("%s : %s" % (
        "Cantidad de coclones", len(coclones)
        ))
    
    # coclones_to_file(
    #     generators, 
    #     logging.getLoggerClass().root.handlers[0].baseFilename[:-3] + "txt"
    # )
    
    return (coclones, generators)