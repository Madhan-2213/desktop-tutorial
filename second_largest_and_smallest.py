def find_second_largest_and_smallest(numbers):
    if len(numbers) < 2:
        return None, None  

    if numbers[0] > numbers[1]:
        largest = numbers[0]
        second_largest = numbers[1]
        smallest = numbers[1]
        second_smallest = numbers[0]
    else:
        largest = numbers[1]
        second_largest = numbers[0]
        smallest = numbers[0]
        second_smallest = numbers[1]

    for i in range(2, len(numbers)):
        number = numbers[i]

        if number > largest:
            second_largest = largest
            largest = number
        elif number > second_largest:
            second_largest = number

        if number < smallest:
            second_smallest = smallest
            smallest = number
        elif number < second_smallest:
            second_smallest = number

    return second_largest, second_smallest

numbers = [34, -50, 23, 0, 89, -345, 27]
second_largest, second_smallest = find_second_largest_and_smallest(numbers)
print("Second largest number:", second_largest)
print("Second smallest number:", second_smallest)
