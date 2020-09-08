#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    i=0
    for i in range(grades_count):
        if grades[i]<=37:
            grades[i]=grades[i]
        elif grades[i]>37:
            j=1
            for j in range(3):
                if (grades[i]+j)%5==0:
                    grades[i]=(grades[i]+j)
                else:
                    grades[i]=grades[i]
    for k in range(grades_count):
        print(grades[k])
            


    

if __name__ == '__main__':

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)
