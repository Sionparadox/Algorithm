import sys
import heapq
input = sys.stdin.readline
INF = float('inf')

def dijkstra(start, graph, L):
    dist = [INF]*L
    dist[start] = 0
    pq = []
    heapq.heappush(pq, (0, start))
    while pq:
        d, curr = heapq.heappop(pq)
        if d>dist[curr]:
            continue
        for nxt, dst in graph[curr]:
            nd = d+dst
            if dist[nxt]>nd:
                dist[nxt] = nd
                heapq.heappush(pq, (nd, nxt))
    
    return dist

T = int(input())
for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    s, g, h = s-1, g-1, h-1
    graph = [[] for _ in range(n)]
    gh = 0
    for _ in range(m):
        a, b, d = map(int, input().split())
        a,b = a-1, b-1
        graph[a].append((b, d))
        graph[b].append((a, d))
        if (a==g and b==h) or (a==h and b==g):
            gh = d

    distS = dijkstra(s, graph, n)
    distG = dijkstra(g, graph, n)
    distH = dijkstra(h, graph, n)
    
    res = []
    for _ in range(t):
        E = int(input())-1
        if distS[E] == INF:
            continue
        if distS[g]+distH[E]+gh == distS[E] or distS[h]+distG[E]+gh == distS[E]:
            res.append(E+1)
    res.sort()
    print(*res)
