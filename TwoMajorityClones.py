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

    for sub in DM2.subuniverses(proper=False):
        binary_relations.add(BinaryRelation(DM.universe, pairs=sub))

    logging.info("%s" % binary_relations)
