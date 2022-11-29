# ソートLv.1の選択ソートを実装
# これの計算量はO(n^2)

import sys
sys.dont_write_bytecode = True # これ入れとかないと実行時に__pycache__が作成される。やめてほしい。

import mklist

#データ準備
data = mklist.gen_list()
print(f'ソート前データ: {data}')

for i in range(len(data)):
    min = i # 最小値の位置をセット
    for j in range(i + 1, len(data)):
        if data[min] > data[j]:
            min = j # 最小値が更新されたらその位置をセット
    # 最小値の位置と現在の要素を交換
    data[i], data[min] = data[min], data[i]

print(f'ソート後データ: {data}')