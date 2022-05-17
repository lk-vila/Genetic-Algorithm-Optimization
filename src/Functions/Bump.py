import math
from queue import Queue
from . import AbstractFunction

class Bump(AbstractFunction.AbstractFunction):
    def calculate(variables: Queue[float]) -> float:
        x = variables.get()
        y = variables.get()

        z: float
        if((x * y) < 0.75):
            z = None
        elif((x+y) > 7.5 * 2):
            z = None
        else:
            temp0 = pow(math.cos(x), 4) + pow(math.cos(y), 4)
            temp1 = 2 * (pow(math.cos(x), 2)) * (pow(math.cos(y), 2))
            temp2 = math.sqrt(pow(x, 2) + 2 * pow(y, 2))
            z = -abs( (temp0 - temp1) / temp2)
            return z