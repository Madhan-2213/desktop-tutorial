from itertools import product
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
print(*list(product(A, B)))
