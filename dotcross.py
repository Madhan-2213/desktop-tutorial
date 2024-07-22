import numpy 
n=int(input())

a=numpy.array([input().split() for _ in range(n)],int)
b=numpy.array([input().split() for _ in range(n)],int)

# b_transpose = numpy.array([[b[i][j] for i in range(n)] for j in range(n)])

b_transpose = b.T

print(numpy.array([[numpy.dot(a[j],b_transpose[i]) for i in range(n)] for j in range(n)]))
