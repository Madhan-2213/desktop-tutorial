def count_elements(input_str):
    char_count = 0
    digit_count = 0
    symbol_count = 0

    for char in input_str:
        if char.isalpha():
            char_count += 1
        elif char.isdigit():
            digit_count += 1
        else:
            symbol_count += 1

    return char_count, digit_count, symbol_count

str1 = "P@#yn26at^&i5ve"
chars, digits, symbols = count_elements(str1)
print("Total counts of chars, digits, and symbols")
print("Chars =", chars)
print("Digits =", digits)
print("Symbols =", symbols)
