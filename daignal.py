#!/bin/python3

import math
import os
import random
import re
import sys
MAX=100
#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    first = 0
    second = 0; 
    for i in range(0, n):  
        for j in range(0, n):  
  
            # Condition for principal diagonal 
            if (i == j): 
                first =first+ arr[i][j] 
  
            # Condition for secondary diagonal 
            if ((i + j) == (n - 1)): 
                second =second + arr[i][j]
    if second>first:
        return second-first
    elif first>second:
        return first-second
    else:
        return 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
