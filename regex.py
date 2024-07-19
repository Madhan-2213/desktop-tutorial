import re

s = input()
k = input()

result = [(i.start(),i.end()+len(k)-1) for i in re.finditer('(?={0})'.format(k), s)]
if len(result) > 0:
    for n in result:
        print(n)
else:
    print((-1,-1))
