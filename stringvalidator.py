      if __name__ == '__main__':
    s = input()
    alnum = alpha = digit = lower = upper =  False 
    for i in s :
        if i.isalnum():
            alnum = True 
        if i.isalpha():
            alpha = True 
        if i.isdigit():
            digit = True 
        if i.islower():
            lower = True 
        if i.isupper():
            upper = True 
        if alnum and alpha and digit and lower and upper:
            break
    print(alnum)
    print(alpha)
    print(digit)
    print(lower)
    print(upper)
