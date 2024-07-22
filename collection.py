from collections import Counter
n = int(input())
available_shoes = list(map(int, (input()).split()))
customers_qty = int(input())
shoes_sizewise_qty = dict(Counter(available_shoes))
customer_desired_shoe_size = []
size_1 = []
money_1 = []


for i in range(customers_qty):
    customer_desired_shoe_size.extend(map(int, (input().split())))

for i in range(len(customer_desired_shoe_size)):
    if i % 2 == 0:
        if customer_desired_shoe_size[i] in shoes_sizewise_qty.keys():
            if shoes_sizewise_qty[customer_desired_shoe_size[i]] >= 1:
                size_1.append(customer_desired_shoe_size[i])
                money_1.append(customer_desired_shoe_size[i+1])
                shoes_sizewise_qty[customer_desired_shoe_size[i]] -= 1

    else:
        pass

total_earning = sum(money_1)


print(total_earning)
