import logging
import sys
import json
import numpy as np
from folpy.utils.parser.parser import Parser

from clon_utils_v1 import op_preserve_relation

def print_usage():
    print("Modo de uso:")
    print("  python check_functions.py <ruta_al_modelo> <ruta_a_las_funciones>")
    print("Ejemplo:")
    print("  python check_functions.py 'Models/DM.model' 'Functions/DM.fun'")
    sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print_usage()
    path_model = sys.argv[1]
    path_fun = sys.argv[2]
    algebra_name = path_model[7:-6]
    functions_name = path_fun[10:-4]
    logging.basicConfig(
        filename='logs/check_functions/%s.log' % functions_name,
        format='%(asctime)s - %(levelname)s: %(message)s',
        level=logging.DEBUG
        )

    functions = Parser(path_fun).parse().operations

    logging.info("Carga de Funciones OK")

    functions_in_matrix = []
    for f in functions:
        shape = (len(functions[f].d_universe),) * functions[f].arity()
        g = np.zeros(shape, dtype=int)
        for idx, val in functions[f].dict.items():
            g[idx] = val
        functions_in_matrix.append(g)

    with open("Models/Relations/%s.json" % algebra_name, "r") as fp:
        relations = json.load(fp)
    
    relations_preserved = []
    for rel in relations:
        preserved = True
        for fun in functions_in_matrix:
            preserved = preserved and op_preserve_relation(fun, rel)
            if not preserved:
                break
        if preserved:
            relations_preserved.append(rel)
            logging.info("Relación %s preservada" % rel)

    print("Relaciones: %s" % len(relations))
    print(relations)
    print("Relaciones preservadas: %s" % len(relations_preserved))
    print(relations_preserved)