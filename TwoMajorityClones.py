import logging

from itertools import chain, combinations 
from folpy.utils.parser.parser import Parser
from binary_relation import BinaryRelation, one_rel_closure, closure_of_union, bottom_relation, top_relation


def powerset_from(iterable, n):
    "powerset_from([1,2,3], 0) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(n, len(s)+1))

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
    losetas = {}

    i=0
    for sub in DM2.subuniverses(proper=False):
        br = BinaryRelation(DM.universe, pairs=sub)
        binary_relations.add(br)
        i += 1
        logging.info("%s : %s %s" % (i, sub, br.repr_by_T()))

        if br == br.repr_by_T():
            closure = one_rel_closure(br)
            if closure not in losetas.values():
                losetas[br] = closure
    
    
    logging.info("%s : %s" % ("Tamaño de losetas", [len(x) for x in losetas.values()]))

    coclones = list(losetas.values()).copy()

    for s in powerset_from(losetas.values(), 2):
        closure = {bottom_relation(br.universe), top_relation(br.universe)}
        for x in s:
            closure = closure_of_union(x, closure)
            if closure not in coclones:
                coclones.append(closure)

    logging.info("%s : %s" % ("Tamaños de coclones", [len(x) for x in coclones]))
    logging.info("%s : %s" % ("Cantidad de coclones", len(coclones)))

