n, m = map(int, input().split())
c1 = "-"
c2 = ".|."
w = "WELCOME"
leng = n//2

for i in range(leng):
    print( ((2*i+1)*c2).center(m, c1))
    
print(w.center(m, c1))

for i in range(leng-1, -1, -1):
    print( ((2*i+1)*c2).center(m,c1))
