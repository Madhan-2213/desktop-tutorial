from itertools import combinations
s, n = input().split()
s = sorted(s)
n = int(n)
combinations_list = []
combined_s = []

for i in range(1, n+1):  
    #combs = 
    combinations_list.append(list(combinations(s, i)))
    
for i in combinations_list:
    for j in i:
        combined_s.append("".join(j))

for i in combined_s:
    print(i)
