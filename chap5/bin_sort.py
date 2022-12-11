# ビンソート
# ソートする値の範囲がわかっていれば早い

import sys
sys.dont_write_bytecode = True # これ入れとかないと実行時に__pycache__が作成される。やめてほしい。

import mklist_for_bin

#データ準備
data = mklist_for_bin.gen_list()
print(f'ソート前データ: {data}')

bucket = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0
}

def count(data, bucket):
    for datum in data:
        bucket[datum] += 1
    return bucket

def output_data(bucket):
    sorted = []
    for key, value in bucket.items():
        for i in range(value):
            sorted.append(key)
    return sorted

def bin_sort(data, bucket):
    bucket = count(data, bucket)
    return output_data(bucket)

sorted_data = bin_sort(data, bucket)
print(f'ソート後データ: {sorted_data}')