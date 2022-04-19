# -*- coding: UTF8 -*-

import sys

input_price = input('Insert: ')
if not str(input_price).isdecimal():
    print('ちゃんと整数を入力してください')
    sys.exit()

product_price = input('Product: ')
if not str(product_price).isdecimal():
    print('ちゃんと整数を入力してください')
    sys.exit()

change = int(input_price) - int(product_price)

if change < 0:
    print('お金が足りないよ？')
    sys.exit()

for i in coin:
    r = change // i
    change %= i
    print("{0}円: {1}枚").format(i, r)