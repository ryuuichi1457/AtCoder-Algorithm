from heapq import heappop,heappush


def dijk(V,node,r):
    start=r
    dist=[float("inf")]*V
    cnf=[False]*V
    dist[start]=0

    q=[(dist[start],start)]

    while q:
        d,now =heappop(q)
        if cnf[now]:continue
        cnf[now]=True
        for next,c in node[now]:
            if not cnf[next]:
                if dist[now]+c<dist[next]:
                    dist[next]=dist[now]+c
                    heappush(q,(dist[next],next))
    return dist

#第二引数のnode の構造について
"""
三次元配列で
[[[各ノードから行ける場所、それに対応するコスト]]]
となっている
0インデックスに注意
"""