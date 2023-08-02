import logging
import json
import sys
import os
from itertools import chain, combinations
from folpy.utils.parser.parser import Parser

from binary_relation import BinaryRelation
from coclon_utils import one_rel_closure, gen_coclones

if __name__ == "__main__":
    path = sys.argv[1]
    logging.basicConfig(
        filename='logs/' + path[7:-6] + '.log',
        format='%(asctime)s - %(levelname)s: %(message)s',
        level=logging.DEBUG
        )

    algebra = Parser(path).parse()

    logging.info("Carga de Modelo OK")

    (coclones, genrators) = gen_coclones(algebra)
