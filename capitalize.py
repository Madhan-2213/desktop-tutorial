#!/bin/python3

import math
import os
import random
import re
import sys

def solve(s):
    words = s.split(" ")
    
    capitalized_words = [word.capitalize() for word in words]
    

    capitalized_full_name = ' '.join(capitalized_words)
    
    return capitalized_full_name
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
