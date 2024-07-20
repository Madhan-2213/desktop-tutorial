import numpy


n, m = input().strip().split()
list = []
for i in range(int(n)):
    l = input().strip().split()
    if len(l)!=int(m):
        raise ValueError(f"Column length must be {m}")
    list.append(l)
arr = numpy.array(list, int)
print(numpy.transpose(arr))
print(arr.flatten())
