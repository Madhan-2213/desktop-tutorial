from collections import OrderedDict

market_dict = OrderedDict()   
num = int(input())
items = [input() for _ in range(num)]
for item_price in items:
    name = item_price.rsplit(' ', 1)[0]
    price = item_price.rsplit(' ', 1)[1]
    if name not in market_dict:
        market_dict[name] = int(price)
    else:
        market_dict[name] += int(price)

[print(key, val) for key, val in market_dict.items()]
