def count_substring(string: str, sub_string: str) -> int:
    
    count: int = 0
    
    for i in range(len(string)):
        if string[i : i + len(sub_string)] == sub_string:
            count += 1
    else:
        return count
