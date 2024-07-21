for i in range(1, int(input())+1):
    print(sum(list(map(lambda a,b: (10**a)*b, list(range(2*i-2, -1, -1)), list(range(1,i))+list(range(i,0,-1))))))
