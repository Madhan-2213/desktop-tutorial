import numpy
arr=[]
a=input().split(" ")
for i in a:
    arr.append(int(i))
a1=numpy.array(arr)
a1.shape=(3,3)
print(a1)



