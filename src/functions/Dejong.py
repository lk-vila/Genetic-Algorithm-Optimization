import math
from typing import List

from Phenotype import Phenotype
from . import AbstractFunction

class Dejong(AbstractFunction.AbstractFunction):
    def calculate(self, variables: List[float], phenotype: Phenotype) -> float:
        x = variables.pop(0)
        y = variables.pop(0)

        z: float = 100 * pow( (pow(x,2) - pow(y,2)), 2) + pow( (1 - pow(x, 2) ), 2)
        phenotype.fitness = z


    def interpretGene(self, gene: List[int]) -> List[float]:
        variables: List = []
        x = super().convertBinList(gene[0:16]) * 0.0001 - 2
        y = super().convertBinList(gene[16:32]) * 0.0001 - 2
        if x > 2:
            x = 2
        if y > 2:
            y = 2

        variables.append(x)
        variables.append(y)
        return variables


    def getGeneLength(self):
        return 32
