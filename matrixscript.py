import os
import random
import re
import sys

def decode(matrix):
    T_matrix = list(zip(*matrix))
    encoded_str = ""
    for line in T_matrix:
        encoded_str += "".join([str(c) for c in line])

    pattern = r"(?<=[0-9A-Za-z])[^0-9A-Za-z]+(?=[0-9A-Za-z])" 
    print(re.sub(pattern, ' ', encoded_str))
        

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

decode(matrix)
