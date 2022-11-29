# 挿入ソート。いっつもよくわからない。何度も書いて覚えるしかない。
# 一時退避領域tempを持っている

import sys
sys.dont_write_bytecode = True # これ入れとかないと実行時に__pycache__が作成される。やめてほしい。

import mklist

#データ準備
data = mklist.gen_list()
print(f'ソート前データ: {data}')

for i in range(1, len(data)):
    temp = data[i]
    j = i - 1
    while (j >= 0) and (data[j] > temp):
        data[j + 1] = data[j] # 要素を1つずつ後ろにずらす
        j -= 1
    data[j + 1] = temp  # 一時領域から戻す

print(f'ソート後データ: {data}')