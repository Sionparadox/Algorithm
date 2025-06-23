import sys
from collections import defaultdict
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())

graph = defaultdict(list)

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u-1].append((v-1, w))
    graph[v-1].append((u-1, w))

dist = [float('inf')]*N
dist[0] = 0
pq =[]
heapq.heappush(pq, (0, 0))
while pq:
    d, pos = heapq.heappop(pq)
    if dist[pos] < d:
        continue
    for nxt, weight in graph[pos]:
        nd = d+weight
        if dist[nxt] > nd:
            dist[nxt] = nd
            heapq.heappush(pq, (nd, nxt))

print(dist[N-1])
        