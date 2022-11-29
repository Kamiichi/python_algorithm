# リストの最小の要素を探して出力する
# Pythonの組み込み関数min()と同じ動き

import sys
sys.dont_write_bytecode = True # これ入れとかないと実行時に__pycache__が作成される。やめてほしい。

import mklist

#データ準備
data = mklist.gen_list()
print(f'ソート前データ: {data}')

# アルゴリズム
min = 0
for i in range(1, len(data)):
    if data[min] > data[i]:
        min = i

print(f'最小のデータはdata[{min}]の値で{data[min]}')