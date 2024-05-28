def append_in_middle(str1, str2):
    length_str1 = len(str1)

    middle_index = length_str1 // 2

    str3 = str1[:middle_index] + str2 + str1[middle_index:]

    return str3

str1 = "STAR"
str2 = "SUPER"
str3 = append_in_middle(str1, str2)
print("Input string 1:", str1)
print("Input string 2:", str2)
print("Output string:", str3)
