# heapify関数を定義して実装の難易度を軽減

import sys
sys.dont_write_bytecode = True # これ入れとかないと実行時に__pycache__が作成される。やめてほしい。

import mklist

#データ準備
data = mklist.gen_list()
print(f'ソート前データ: {data}')

def heapify(data, i):
    left = 2 * i + 1
    right = 2 * i + 2
    size = len(data) - 1
    min = i
    if left <= size and data[min] > data[left]: #左下の方が小さい時
        min = left
    if right <= size and data[min] > data[right]: # 右下の方が小さい時
        min = right
    if min != i: # 交換が発生する時
        data[i], data[min] = data[min], data[i]
        heapify(data, min)  #ヒープを再構成

# ヒープを構成
for i in reversed(range(len(data) // 2)): #　葉ノード以外を処理
    heapify(data, i)

# ソートを実行
sorted_data = []
for _ in range(len(data)):
    data[0], data[-1] = data[-1], data[0] # 最小のノードと先頭を入れ替え
    sorted_data.append(data.pop())  # 最小のノードを取り出してソート済みにする
    heapify(data, 0) # ヒープを再構成

print(f'ソート後のデータ: {sorted_data}')