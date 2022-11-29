# 改良されたバブルソート。
# 入れ替えが発生しない場合 == ソート済みである場合に以降の処理はスキップさせる。

import sys
sys.dont_write_bytecode = True # これ入れとかないと実行時に__pycache__が作成される。やめてほしい。

import mklist

#データ準備
data = mklist.gen_list()
print(f'ソート前データ: {data}')

change = True
for i in range(len(data)):
    if not change:  # 交換が発生していなければ終了
        break
    change = False  # 交換が発生していないものとする
    for j in range(len(data) - i - 1):
        if data[j] > data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]
            change = True   # 交換が発生した

print(f'ソート後データ: {data}')