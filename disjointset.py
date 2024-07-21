happiness = 0
ints = input()
array = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

for i in array:
  if i in A:
    happiness += 1
  elif i in B:
    happiness -= 1
    
print(happiness)
