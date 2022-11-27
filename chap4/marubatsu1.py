import random

goal = [
    0b111000000, 0b000111000, 0b000000111, # 横揃い
    0b100100100, 0b010010010, 0b001001001, # 縦揃い
    0b100010001, 0b001010100               # ななめ揃い
]

# 3つ並んだか判定
def check(player):
    for mask in goal:
        if player & mask == mask:
            return True
    return False

# 交互に置く
def play(p1, p2):
    if check(p2):    # 3つ並んでいたら出力して終了
        print("決着！")
        print([bin(p1), bin(p2)])
        return
    
    board = p1 | p2
    if board == 0b111111111: #全て置いたら引き分けで終了
        print("引き分け！")
        print([bin(p1), bin[p2]])
        return
    # 置ける場所を探す
    w = [i for i in range(9) if (board & (1 << i)) == 0]
    # ランダムに置いてみる
    r = random.choice(w)
    play(p2, p1 | (1 << r))

play(0,0)