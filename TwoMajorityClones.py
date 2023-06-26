import logging

from folpy.utils.parser.parser import Parser
from binary_relation import BinaryRelation


if __name__ == "__main__":
    logging.basicConfig(
        filename='TwoMajorityClones.log',
        format='%(asctime)s - %(levelname)s: %(message)s',
        level=logging.DEBUG
        )

    DM = Parser("Models/DM.model").parse()

    logging.info("Carga de Modelo OK")

    DM2 = DM * DM

    binary_relations = set()

    i=0
    for sub in DM2.subuniverses(proper=False):
        br = BinaryRelation(DM.universe, pairs=sub)
        binary_relations.add(br)
        i += 1
        logging.info("%s : %s %s" % (i, sub, br))
