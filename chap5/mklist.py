# ソート用の素材提供モジュール
# ランダムにリストを出力するよ
import random

def gen_list():
    l = [random.randint(0, 20) for i in range(10)]
    return l