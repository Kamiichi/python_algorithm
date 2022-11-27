floor = int(input())

def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)

if floor == 1 or floor == 2:                          #地上階しかない建物にエレベーターつけちゃダメよ。2階までしかない建物ならこれも1パターンしかない。歩きなさい。
    count = 1
elif floor > 2:
    count = factorial(floor - 2)        #仕様から地上階と最上階は必ず通過するため含めない
    count += 2                          #除いていた2パターンを追加。全フロアに停車パターン + 地上階から直上階まで直通
else:
    count = 0
    print("そんな建物はないよ")

print(f'停止パターンは{count}通り')