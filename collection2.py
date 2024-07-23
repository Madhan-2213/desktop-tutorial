from collections import deque
N = int(input())
lines, d = [input().split() for i in range(N)], deque()
commands, elements = [line[0] for line in lines], [line[1] if len(line) == 2 else '' for line in lines]
[getattr(deque, commands[i])(d, elements[i]) if elements[i] != '' else getattr(deque, commands[i])(d) for i in range(N)]
print(*[d1 for d1 in d])
