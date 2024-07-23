from itertools import permutations
list_1 = list(map(str, (input().split())))
n = ""
k = []
n = int(list_1[1])
for i in list_1[0]:
    k.append(i)    
permut_sets = list(permutations(k, n))
joined_sets = []
for i in permut_sets:
    joined_sets.append("".join(i))
sorted_sets = sorted(joined_sets)
for i in sorted_sets:
    print(i)
