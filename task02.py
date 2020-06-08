import numpy as np 
import random

def throw():

    result = [random.randrange(1,7) for a in range(10)]
    return np.array(result)

if __name__ == "__main__":
    
    simulations = 500
    chances = 0
    x = 0

    print("number of simulations : {0}".format(simulations))
    for simulations in range(simulations):
        result = throw()
        if np.sum(result) == 32:
            chances += 1
    print("possible chances sum in 32 : {0}".format(chances))

    if chances > 0 :
        x = (chances / simulations)
    print("chance of sum 32 in throws : {0}".format(x))