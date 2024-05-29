
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_numbers = [num for num in numbers if num % 2 != 0]
even_numbers = [num for num in numbers if num % 2 == 0]

odd_squares = [num ** 2 for num in odd_numbers]
even_squares = [num ** 2 for num in even_numbers]

print("Odd numbers:", odd_numbers)
print("Even numbers:", even_numbers)
print("Squares of odd numbers:", odd_squares)
print("Squares of even numbers:", even_squares)
