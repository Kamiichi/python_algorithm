# お釣りの金額を求める
insert_price = input('insert: ')
product_price = input('product: ')
change = int(insert_price) - int(product_price)

# 5000札の枚数を求める
r5000 = change // 5000
q5000 = change % 5000
print('5000: {0}枚').format(r5000)

# 1000札の枚数を求める
r1000 = q5000 // 1000
q1000 = q5000 % 1000
print('1000: {0}枚').format(r1000)

# 500円玉の枚数を求める
r500 = q1000 // 500
q500 = q1000 % 500
print('500: {0}').format(r500)

# 100円玉の枚数を求める
r100 = q500 // 100
q100 = q500 % 100
print('100: {0}').format(r100)

# 50円玉の枚数を求める
r50 = q100 // 50
q50 = q100 % 50
print('50: {0}').format(r50)

# 10円玉の枚数を求める
r10 = q50 // 10
q10 = q50 % 10
print('10: {0}').format(r10)

# 5円玉の枚数を求める
r5 = q10 // 5
q5 = q10 % 5
print('5: {0}').format(r5)

# 1円玉の枚数を求める
print('1: {0}').format(q5)
