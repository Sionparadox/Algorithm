import sys, heapq
input = sys.stdin.readline
INF = float('inf')

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

s, t = map(int, input().split())

dist = [INF]*(N+1)
dist[s] = 0
pq = []
heapq.heappush(pq, (0, s))

while pq:
    cost, curr = heapq.heappop(pq)
    
    if dist[curr] < cost:
        continue
    
    for nxt, ncost in graph[curr]:
        new_cost = cost+ncost
        if dist[nxt] > new_cost:
            dist[nxt] = new_cost
            heapq.heappush(pq, (new_cost, nxt))

print(dist[t])
