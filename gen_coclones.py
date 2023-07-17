import logging
import json
import sys
import os
from itertools import chain, combinations
from folpy.utils.parser.parser import Parser

from binary_relation import BinaryRelation
from coclon_utils import one_rel_closure, generate_coclones_by_antichains

if __name__ == "__main__":
    path = sys.argv[1]
    logging.basicConfig(
        filename='logs/' + path[7:-6] + '.log',
        format='%(asctime)s - %(levelname)s: %(message)s',
        level=logging.DEBUG
        )

    algebra = Parser(path).parse()

    logging.info("Carga de Modelo OK")

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

    coclones = generate_coclones_by_antichains(tiles)

    logging.info("%s : %s" % ("Tamaños de coclones anticadenas", [len(x) for x in coclones]))
    logging.info("%s : %s" % ("Cantidad de coclones anticadenas", len(coclones)))
