def bubble_sort_ascending(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

def bubble_sort_descending(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] < numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

numbers = [5, 3, 7, 9, 8, 4, 2]

sorted_ascending = bubble_sort_ascending(numbers.copy())  
print("Ascending Order:", sorted_ascending)

sorted_descending = bubble_sort_descending(numbers.copy())  
print("Descending Order:", sorted_descending)
