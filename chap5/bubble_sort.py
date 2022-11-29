# 直感的にとてもわかりやすいバブルソート
# 一生懸命ソートしてる感があって好き
# 速くはないO(n^2)の計算量

import sys
sys.dont_write_bytecode = True # これ入れとかないと実行時に__pycache__が作成される。やめてほしい。

import mklist

#データ準備
data = mklist.gen_list()
print(f'ソート前データ: {data}')

for i in range(len(data)):
    for j in range(len(data) - i - 1):
        if data[j] > data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]

print(f'ソート後データ: {data}')