import math
import os
import random
import re
import sys

def sockMerchant(n, ar):
    sock = dict()
    c=0
    # storing frequency in dictionary
    for i in ar:
        if i in sock:
            sock[i]=sock[i]+1
        else:
            sock[i]=1
    for key in sock:
        c=int(c+sock[key]//2)
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
