import logging
import sys
import json
from folpy.utils.parser.parser import Parser

from coclon_utils import gen_coclones
from coclon_lattice import (gen_coclon_lattice, gen_meet_irr_lattice, 
                            gen_join_irr_lattice, 
                            gen_meet_irr_and_join_irr_lattice)

def print_usage():
    print("Modo de uso:")
    print("  python check_functions.py <ruta_a_las_funciones>")
    print("Ejemplo:")
    print("  python check_functions.py 'Functions/DM.fun'")
    sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print_usage()
    path = sys.argv[1]
    algebra_name = path[10:-4]
    logging.basicConfig(
        filename='logs/check_functions/%s.log' % algebra_name,
        format='%(asctime)s - %(levelname)s: %(message)s',
        level=logging.DEBUG
        )

    functions = Parser(path).parse().operations

    logging.info("Carga de Funciones OK")

