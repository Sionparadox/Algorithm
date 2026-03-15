import sys, heapq
input = sys.stdin.readline
INF = float('inf')

N, M, K = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, c = map(int, input().split())
    graph[v].append((u, c))

endpoint = list(map(int ,input().split()))

dist = [INF]*(N+1)
dist[0] = 0
pq = []
for e in endpoint:
    dist[e] = 0
    heapq.heappush(pq, (0, e))


while pq:
    d, node = heapq.heappop(pq)
    if dist[node] < d:
        continue
    for nxt, c in graph[node]:
        if dist[nxt] > d+c:
            dist[nxt] = d+c
            heapq.heappush(pq, (d+c, nxt))

max_d = max(dist)
print(dist.index(max_d))
print(max_d)

'''
면접장 -> 각 도시로 다익스트라
 : 도로를 뒤집어서 넣음

'''