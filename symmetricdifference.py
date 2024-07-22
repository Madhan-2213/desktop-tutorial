M1 = int(input())
a1 = set(list(map(int, input().split())))
N1 = int(input())
b1 = set(list(map(int, input().split())))

t = a1.union(b1)
w = a1.intersection(b1)
d = t.difference(w)

for i in sorted(list(d)):
    print(i)
