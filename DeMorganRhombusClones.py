import logging

from folpy.utils.parser.parser import Parser
from binary_relation import BinaryRelation


if __name__ == "__main__":
    logging.basicConfig(
        filename='DeMorganRhombusClones.log',
        format='%(asctime)s - %(levelname)s: %(message)s',
        level=logging.DEBUG
        )

    DMR = Parser("Models/DeMorganRhombus.model").parse()

    logging.info("Carga de Modelo OK")

    DMR2 = DMR * DMR

    binary_relations = []
    
    i=0
    for sub in DMR2.subuniverses(proper=False):
        br = BinaryRelation(DMR.universe, pairs=sub)
        binary_relations.append(br)
        i += 1
        logging.info("%s : %s %s" % (i, sub, br))

