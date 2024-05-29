def find_index(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1  

a = [45, 67, 83, 24, 55, 87, 77, 34]
target = 55
position = find_index(a, target)
print("Position of", target, ":", position)
