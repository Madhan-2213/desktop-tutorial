from itertools import product
K, M = map(int, input().split())
Ls = [map(int, input().split()[1:]) for i in range(K)]
def combs(*args):
    cs = list(product(*args))
    return [sum(c**2 for c in c1) % M for c1 in cs]
print(max(combs(*Ls)))
