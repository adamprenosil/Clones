import logging
import sys
from folpy.utils.parser.parser import Parser

from coclon_utils import gen_coclones
from clon_utils_v2 import gen_clones

if __name__ == "__main__":
    path = sys.argv[1]
    algebra_name = path[7:-6]
    logging.basicConfig(
        filename='logs/clones/%s.log' % algebra_name,
        format='%(asctime)s - %(levelname)s: %(message)s',
        level=logging.DEBUG
        )

    algebra = Parser(path).parse()

    logging.info("Carga de Modelo OK")

    (coclones, generators) = gen_coclones(algebra)

    clones = gen_clones(algebra, (coclones, generators))

    logging.info("Clones: %s" % clones)



