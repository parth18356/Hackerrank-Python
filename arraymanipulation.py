#!/bin/python3

import math
import os
import random
import re
import sys

import itertools as it

def arrayManipulation(n, queries):
    q = it.chain.from_iterable([(a, k), (b, -k)] for a, b, k in queries)
    return max(it.accumulate(c for _, c in sorted(q, key=lambda x: (x[0], -x[1]))))

if __name__ == '__main__':
if __name__ == '__main__':

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)
