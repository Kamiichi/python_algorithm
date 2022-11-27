def hanoi(n, src, dist, via): #src=移動元, dist=移動先, via=経由場所
    if n > 1:
        hanoi(n - 1, src, via, dist)    # n-1枚を移動元から経由場所に移す
        print(src + ' -> ' + dist)
        hanoi(n - 1, via, dist, src)    # n-1枚を経由場所から移動先に移す
    else:
        print(src + ' -> ' + dist)

# インプットのnによる移動回数の参考
# n=10, 1,023回
# n=24, 16,777,215回
# n=64, 1845京
n = int(input())
hanoi(n, 'a', 'b', 'c')