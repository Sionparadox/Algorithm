import sys, heapq
input = sys.stdin.readline
INF = float('inf')

N, M = map(int, input().split())
visible = list(map(int, input().split()))
graph = [[] for _ in range(N)]

for _ in range(M):
    u, v, time = map(int, input().split())
    if (u != N-1 and visible[u]) or (v != N-1 and visible[v]):
        continue
    graph[u].append((v, time))
    graph[v].append((u, time))

dist = [INF]*N
dist[0] = 0
if visible[0]:
    print(-1)
    exit()

pq = []
heapq.heappush(pq, (0, 0))
while pq:
    time, curr = heapq.heappop(pq)
    
    if dist[curr] < time:
        continue
    
    for nxt, nt in graph[curr]:
        new_time = time+nt
        if dist[nxt] > new_time:
            dist[nxt] = new_time
            heapq.heappush(pq, (new_time, nxt))    

print(dist[N-1] if dist[N-1] != INF else -1)
