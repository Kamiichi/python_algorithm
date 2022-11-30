# ヒープソート。ヒープを考えた人は天才。
# 計算量はO(nlogn)

import sys
sys.dont_write_bytecode = True # これ入れとかないと実行時に__pycache__が作成される。やめてほしい。

import mklist

#データ準備
data = mklist.gen_list()
print(f'ソート前データ: {data}')

# ヒープを構成
for i in range(len(data)):
    j = i
    while (j > 0) and (data[(j - 1) // 2] < data[j]):
        data[(j - 1) // 2], data[j] = data[j], data[(j - 1) // 2] # 親と交換
        j = (j - 1) // 2 # 親の位置に移動

# ソートを実行
for i in range(len(data), 0, -1):
    # ヒープの先頭と交換
    data[i - 1], data[0] = data[0], data[i - 1]
    j = 0 # ヒープの先頭から開始
    while ((2 * j + 1 < i - 1) and (data[j] < data[2 * j + 1]))\
        or ((2 * j + 2 < i - 1) and (data[j] < data[2 * j + 2])):
        if (2 * j + 2 == i - 1) or (data[2 * j + 1] > data[2 * j + 2]):
            data[j], data[2 * j + 1] = data[2 * j + 1], data[j]
            j = 2 * j + 1
        else:
            data[j], data[2 * j + 2] = data[2 * j + 2], data[j]
            j = 2 * j + 2

print(f'ソート後データ: {data}')