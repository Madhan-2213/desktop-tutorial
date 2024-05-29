def most_frequent_element(numbers):
    if not numbers:
        return None  

    frequency = {}
    max_count = 0
    most_frequent = numbers[0]

    for number in numbers:
        if number in frequency:
            frequency[number] += 1
        else:
            frequency[number] = 1

        if frequency[number] > max_count:
            max_count = frequency[number]
            most_frequent = number

    return most_frequent


a = [4, 5, 6, 4, 6, 7, 4, 2, 4, 8, 4]
result = most_frequent_element(a)
print("Most frequent element:", result)
