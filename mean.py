import numpy as np

n, m = map(int, input().split())
A = np.array([[*map(int, input().split())] for i in range(n)])

print(np.mean(A, axis=1))
print(np.var(A, axis=0))
print(round(np.std(A), 11))
