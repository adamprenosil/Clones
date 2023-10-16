import logging
import sys
from folpy.utils.parser.parser import Parser

from coclon_utils import gen_coclones
from coclon_lattice import gen_coclon_lattice

if __name__ == "__main__":
    path = sys.argv[1]
    algebra_name = path[7:-6]
    logging.basicConfig(
        filename='logs/%s.log' % algebra_name,
        format='%(asctime)s - %(levelname)s: %(message)s',
        level=logging.DEBUG
        )

    algebra = Parser(path).parse()

    logging.info("Carga de Modelo OK")

    (coclones, generators) = gen_coclones(algebra)

    lattice = gen_coclon_lattice(coclones)

    #lattice.draw()

    lattice.to_file("Models/%sCoclonesLattice.model" % algebra_name)


