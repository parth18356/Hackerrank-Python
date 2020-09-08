#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the reverseArray function below.
def reverseArray(arr):
    stack = []
    arr2=[]
    for i in range(len(arr)):
        stack.append(arr[i])
    for j in range(len(arr)):
        m=stack.pop()
        arr2.append(m)       
    print(*(arr2))
        
    
if __name__ == '__main__':

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)
