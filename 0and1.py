import numpy

shape = [*map(int, input().split())]

print(numpy.zeros(shape, dtype=int))
print(numpy.ones(shape, dtype=int))
