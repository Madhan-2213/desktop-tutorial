import re

for i in range(int(input())):
    inp = str(input())
    [print("YES") if bool(re.search(r'^[789](\d{9})$', inp) ) else print("NO")]
