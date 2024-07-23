import sys
lines = sys.stdin.readlines()
A, s = set(map(int, lines[1].split())), int(lines[2])
commands = []
for i in range(s):
    command, num = lines[3 + 2 * i].split()
    lst = list(map(int, lines[4 + 2 * i].split()))
    func = getattr(set, command)
    func(A, lst)
print(sum(a for a in A))
