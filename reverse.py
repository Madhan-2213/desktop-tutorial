import numpy

def arrays(arr):
    a1=numpy.array(arr,float)
    return a1[::-1]


arr = input().strip().split(' ')
result = arrays(arr)
print(result)
