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
    print("  python gen_coclones.py <ruta_al_modelo>")
    print("Ejemplo:")
    print("  python gen_coclones.py 'Models/DM.model'")
    sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print_usage()
    path = sys.argv[1]
    algebra_name = path[7:-6]
    logging.basicConfig(
        filename='logs/coclones/%s.log' % algebra_name,
        format='%(asctime)s - %(levelname)s: %(message)s',
        level=logging.DEBUG
        )

    algebra = Parser(path).parse()
    algebra.name = algebra_name
    
    logging.info("Carga de Modelo OK")

    (coclones, generators) = gen_coclones(algebra)

    lattice = gen_coclon_lattice(coclones)
    
    lattice.draw()

    gen_meet_irr_lattice(lattice).draw()
    gen_join_irr_lattice(lattice).draw()
    gen_meet_irr_and_join_irr_lattice(lattice).draw()

    lattice.to_file("Models/CoclonesLattices/%s.model" % algebra_name)

    coclones_dict = {i : [coclon.list_of_pairs() for coclon in coclones[i]] 
                     for i in range(len(coclones))}

    with open("Models/CoclonesUniverses/%s.json" % algebra_name, "w") as fp:
        json.dump(coclones_dict, fp)  # encode dict into JSON


