# ビンソート用の素材提供モジュール
# 0-9の数値をランダムにリストを出力するよ
import random

def gen_list():
    l = [random.randint(0, 9) for i in range(20)]
    return l