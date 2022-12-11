# マージソート
# ここから計算が早くなってくる

import sys
sys.dont_write_bytecode = True # これ入れとかないと実行時に__pycache__が作成される。やめてほしい。

import mklist

#データ準備
data = mklist.gen_list()
print(f'ソート前データ: {data}')

def merge_sort(data):
    if len(data) <= 1:
        return data
    
    mid = len(data) // 2 # 半分の位置を計算
    # 再帰的に分割
    left = merge_sort(data[:mid]) # 左側を分割
    right = merge_sort(data[mid:]) # 右側を分割
    # 結合
    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0

    while (i < len(left)) and (j < len(right)):
        if left[i] <= right[j]: # 左<=右のとき
            result.append(left[i])  #　左側から1つ取り出して追加
            i += 1
        else:
            result.append(right[j]) # 右側から1つ取り出して追加
            j += 1
    
    # 残りをまとめて追加
    if i < len(left):
        result.extend(left[i:]) # 左側の残りを追加
    if j < len(right):
        result.extend(right[j:]) # 右側の残りを追加
    return result

sorted_data = merge_sort(data)
print(f'ソート前データ: {sorted_data}')