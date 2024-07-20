from datetime import datetime

import math
import os
import random
import re
import sys

# Complete the time_delta function below.
def time_delta(t1, t2):
    delta1 = datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    delta2 = datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
    diff = abs(delta2-delta1).total_seconds()
    return str(int(diff))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
