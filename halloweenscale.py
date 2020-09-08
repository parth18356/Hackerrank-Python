#!/bin/python3

import math
import os
import random
import re
import sys
from operator import add
from itertools import accumulate
from operator import add


# Complete the howManyGames function below.
def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    o=[]
    i=0
    j=0
    x=[]
    while (p-(d*i))>=m :
        q=(p-(d*i))
        i=i+1
        o.append(q)
    for i in range(11000):
        o.append(m)
    lol=list(accumulate(o,add))
    k=0
    for k in lol:
        if k>s:
            x.append(k)
    for h in x:
        if h in lol:
            lol.remove(h)
    print(len(lol))
        
        
        

if __name__ == '__main__':

    pdms = input().split()

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)
