def average(array):
   
    st = list(set(array))
    avg = sum(st)/len(st)
    return float("{:.3f}".format(avg))
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
