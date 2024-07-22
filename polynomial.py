from numpy import array, polyval

print(polyval(array(list(map(float, input().split()))), int(input())))
