def create_new_string(input_str):
 
    length = len(input_str)

    middle_index = length // 2

   
    first_char = input_str[0]
    middle_char = input_str[middle_index]
    last_char = input_str[-1]

   
    new_string = first_char + middle_char + last_char

    return new_string

input_str = "PRADEEP"
output_str = create_new_string(input_str)
print("Input string:", input_str)
print("Output string:", output_str)
