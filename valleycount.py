import math
import os
import random
import re
import sys

def countingValleys(steps, path):
    lvl=0
    vallcount=0
    for st in range(0,steps):
        if path[st]=='U':
            lvl+=1
        if path[st]=='D':
            lvl-=1
        # we are in a valley if we are currently in sea level(i.e 0) and next we have U
        if path[st]=='U' and lvl==0:
            vallcount +=1
    return vallcount 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
