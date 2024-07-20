import re
p = r'(?<!^)(#[A-Fa-f0-9]{6}|#[A-Fa-f0-9]{3})'
n = int(input())

for _ in range(n):
    x = input()
    y = re.findall(p, x)
    if len(y):  # Checking len() isn't required here.
        for i in y:
            print(i)
