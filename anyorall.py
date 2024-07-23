inte, ints = int(input()), list(map(int, input().split()))
print(all(a > 0 for a in ints) and any(str(a) == str(a)[::-1] for a in ints))
