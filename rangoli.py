a_ord = ord('a') - 1
    
def build_pattern(start, jump_size):
    l = []
    for i in range(jump_size):
        l.append(chr(start - i))
    l.extend(reversed(l[:jump_size-1]))
    return "-".join(l)

def print_rangoli(size):
    length = 4 * size - 3
    start = a_ord + size
    
    # top + middle
    for i in range(1, size + 1):
        pattern = build_pattern(start, i)
        print(f'{pattern}'.center(length,'-'))
    # bottom
    for i in range(size-1,0,-1):
        pattern = build_pattern(start, i)
        print(f'{pattern}'.center(length,'-'))
