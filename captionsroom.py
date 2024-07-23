import sys
lines = sys.stdin.readlines()
n, lst = int(lines[0]), list(map(int, lines[1].split()))
lstset = set(lst)
[lst.remove(i) for i in lstset]
print(sum(lstset.difference(lst)))
