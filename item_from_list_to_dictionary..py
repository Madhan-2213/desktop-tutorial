keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

dictionary = {}

for key, value in zip(keys, values):
    dictionary.update({key: value})

print(dictionary)
