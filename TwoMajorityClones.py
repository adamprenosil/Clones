import logging

from folpy.utils.parser.parser import Parser



if __name__ == "__main__":
    logging.basicConfig(
        filename='TwoMajorityClones.log',
        format='%(asctime)s - %(levelname)s: %(message)s',
        level=logging.DEBUG
        )

    DM = Parser("Models/DM.model").parse()

    logging.info("Carga de Modelo OK")

    DM2 = DM * DM

    logging.info("%s" % list(DM2.subuniverses()))
