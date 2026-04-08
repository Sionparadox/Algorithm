import sys, heapq
input = sys.stdin.readline
INF = float('inf')

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

s, e = map(int, input().split())

dist = [0]*(N+1)

pq = []
dist[s] = INF
heapq.heappush(pq, (-INF, s))

while pq:
    w, curr = heapq.heappop(pq)
    w = -w
    
    if dist[curr] > w:
        continue
    
    for nxt, weight in graph[curr]:
        nw = min(w, weight)
        if nw > dist[nxt]:
            dist[nxt] = nw
            heapq.heappush(pq, (-nw, nxt))

print(dist[e])