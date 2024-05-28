def create_new_string(s1, s2):
    s3 = ""

    len_s1 = len(s1)
    len_s2 = len(s2)

    max_len = max(len_s1, len_s2)

    for i in range(max_len):
        if i < len_s1:
            s3 += s1[i]
        if i < len_s2:
            s3 += s2[-(i + 1)]  
    return s3


s1 = "Abc"
s2 = "Xyz"
output = create_new_string(s1, s2)
print("Output:", output)
