def print_formatted(number):
    w = len(bin(number)[2:])
    for i in range(1, number + 1):
        l = [oct(i), hex(i), bin(i)]
        l = list(map(lambda x: x[2:].upper(), l))
        l.insert(0, str(i))
        l = map(lambda x: x.rjust(w), l)
        print(" ".join(l))
