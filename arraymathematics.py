import numpy
n, m = map(int, input().split())
A = numpy.array([[*map(int, input().split())] for _ in range(n)])
B = numpy.array([list(map(int, input().split())) for _ in range(n)])

print(A + B)
print(numpy.subtract(A, B))
print(numpy.multiply(A, B))
print(A//B)
print(numpy.mod(A, B))
print(numpy.power(A, B))


