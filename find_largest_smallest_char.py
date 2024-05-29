def find_largest_and_smallest(numbers):
    if len(numbers) == 0:
        return None, None  

    largest = numbers[0]
    smallest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number
        if number < smallest:
            smallest = number

    return largest, smallest

numbers = [34, -50, 23, 0, 89, -345, 27]
largest, smallest = find_largest_and_smallest(numbers)
print("Largest number:", largest)
print("Smallest number:", smallest)
