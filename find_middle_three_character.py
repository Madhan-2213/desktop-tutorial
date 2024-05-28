def get_middle_three_chars(input_str):
    length = len(input_str)

    if length < 3:
        return "Input string must be at least 3 characters long."

    middle_index = length // 2

    middle_three_chars = input_str[middle_index - 1:middle_index + 2]

    return middle_three_chars


input_str = "PRADEEP"
output_str = get_middle_three_chars(input_str)
print("Input string:", input_str)
print("Output string:", output_str)
