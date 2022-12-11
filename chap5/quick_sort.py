# クイックソート
# 速い！

import sys
sys.dont_write_bytecode = True # これ入れとかないと実行時に__pycache__が作成される。やめてほしい。

import mklist

#データ準備
data = mklist.gen_list()
print(f'ソート前データ: {data}')

def quick_sort(data):
    if len(data) <= 1:
        return data
    
    pivot = data[0] # ピボットとしてリストの先頭を使用
    left, right, same = [], [], 0

    for i in data:
        if i < pivot:
            # ピボットより小さい場合には左に
            left.append(i)
        elif i > pivot:
            # ピボットより大きい場合には右に
            right.append(i)
        else:
            same += 1
    
    left = quick_sort(left) # 左側をソート
    right = quick_sort(right) # 右側をソート
    # ソートされたものとピボットの値を合わせて返す
    return left + [pivot] * same + right

sorted_data = quick_sort(data)
print(f'ソート後データ: {sorted_data}')