import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline
INF = float('inf')

def dijkstra(start, n):
    dist = [INF]*(n+1)
    dist[start] = 0
    pq = []
    heapq.heappush(pq, (0, start))
    while pq:
        d, node = heapq.heappop(pq)
        if dist[node] < d: continue
        for nxt, t in graph[node]:
            nd = d+t
            if dist[nxt]>nd:
                dist[nxt] = nd
                heapq.heappush(pq, (nd, nxt))
    return dist


T = int(input())
for _ in range(T):
    n, d, c = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a, s))
    
    dist = dijkstra(c, n)
    cnt = 0
    max_val = 0
    for i in range(1, n+1):
        if dist[i] == INF: continue
        cnt += 1
        max_val = max(max_val, dist[i])
    
    print(cnt, max_val)
