to_sort = input()
sorted_str = ("".join(sorted(to_sort, key=lambda x: (x.isdigit(), x.isdigit() and int(x) % 2 == 0, x.isupper(), x))))
print(sorted_str)
