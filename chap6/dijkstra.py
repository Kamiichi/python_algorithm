def dijkstra(edges, num_v):
    dist = [float('inf')] * num_v
    dist[0] = 0
    q = [i for i in range(num_v)]

    while len(q) > 0:
        # 最もコストが小さい頂点を探す
        r = q[0]
        for i in q:
            if dist[i] < dist[r]:
                r = i   # コストが小さい点が見つかると更新
        
        # 最もコストが小さい頂点を取り出す
        u = q.pop(q.index(r))
        for i in edges[u]:  # 取り出した頂点からの辺を繰り返し
            if dist[i[0]] > dist[u] + i[1]:
                # 頂点までのコストが更新できれば更新
                dist[i[0]] = dist[u] + i[1]
    return dist

# 辺のリスト(終点とコストのリスト)
edges = [
    [[1, 4], [2, 3]],   # 頂点Aからの辺のリスト
    [[2, 1], [3, 1], [4, 5]],   # 頂点Bからの辺のリスト
    [[5, 2]],   #頂点Cからの辺のリスト
    [[4, 3]],   # 頂点Dからの辺のリスト
    [[6, 2]],   # 頂点Eからの辺のリスト
    [[4, 1], [6, 4]],   # 頂点Fからの辺のリスト
    []  # 頂点Gからの辺のリスト
]

print(dijkstra(edges, 7))