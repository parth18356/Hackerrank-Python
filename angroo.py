#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    l=[]
    m=[]
    count=0
    i=0
    for i in range(50000):
        p=x1+(v1*i)
        l.append(p)
    for j in range(50000):
        q=x2+(v2*j)
        m.append(q)
    #print(l)
    #print(m)
    for k in range(50000):
        if l[k]==m[k]:
            count=count+1
        else:
            count=count
    #print(count)
    if count==0:
        print("NO")
    elif count>=1:
        print("YES")
            

if __name__ == '__main__':

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

