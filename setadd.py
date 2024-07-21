import sys

if __name__ == '__main__':
    lines = sys.stdin.readlines()
    names, countries = lines[1:int(lines[0]) - 1], []
    [countries.append(n) for n in names]
    print(len(set(countries)))
