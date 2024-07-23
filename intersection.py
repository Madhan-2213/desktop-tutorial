n = int(input())
m = set(list(map(int, input().split())))
r = int(input())
e = set(list(map(int, input().split())))

t = m.intersection(e)

print(len(t))
