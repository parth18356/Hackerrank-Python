#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    for i in range(apples_length):
        apples[i]=apples[i]+a
    for j in range(oranges_length):
        oranges[j]=oranges[j]+b
    count=0
    for k in range(apples_length):
        if apples[k]>=s and apples[k]<=t:
            count=count+1
    print(count)
    lol=0
    for p in range(oranges_length):
        if oranges[p]>=s and oranges[p]<=t:
            lol=lol+1
    print(lol)
            
    
if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))
    apples_length=len(apples)

    oranges = list(map(int, input().rstrip().split()))
    oranges_length=len(oranges)

    countApplesAndOranges(s, t, a, b, apples, oranges)
