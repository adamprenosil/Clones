import logging
import sys
from folpy.utils.parser.parser import Parser

from coclon_utils import gen_coclones
from coclon_lattice import draw_coclon_lattice

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

    draw_coclon_lattice(coclones)


