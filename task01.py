import numpy as np 
import random

def checking_dices():
    x = 0
    for d1 in range(1,7):
        for d2 in range(1,7):
            for d3 in range(1,7):
                for d4 in range(1,7):
                    for d5 in range(1,7):
                        for d6 in range(1,7):
                            for d7 in range(1,7):
                                for d8 in range(1,7):
                                    for d9 in range(1,7):
                                        for d10 in range(1,7):
                                            if(d1+d2+d3+d4+d5+d6+d7+d8+d9+d10)==32:
                                                x += 1
    print("\t number of total 32 chances : {}".format(x))
    return x

if __name__ == "__main__" :

    total_chances = checking_dices()
    total_nubof_chances = 6 ** 10
    print("\t total No.of chances : {}".format(total_nubof_chances))
    print("\t chances : {}".format(total_chances/total_nubof_chances))

