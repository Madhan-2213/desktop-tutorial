from itertools import combinations
N, string, K = int(input()), list(input().split()), int(input())
combs = list(combinations([i for i in range(N)], K))
tups = [p for p in combs if any(string[p[i]] == 'a' for i in range(K))]
print(len(tups)/len(combs))
