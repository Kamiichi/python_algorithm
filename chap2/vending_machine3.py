# -*- coding: UTF8 -*-

input_price = input('Insert: ')
product_price = input('Product: ')
change = int(input_price) - int(product_price)

coin = [5000, 1000, 500, 100, 50, 10, 5, 1]

for i in coin:
    r = change // i
    change %= i
    print("{0}円: {1}枚").format(i, r)