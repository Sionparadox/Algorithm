import sys, heapq
input = sys.stdin.readline
INF = float('inf')

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, t = map(int, input().split())
    graph[u].append((v, t))
    graph[v].append((u, t))

parent = list(range(N+1))
dist = [INF]*(N+1)
dist[1] = 0
pq = [(0, 1)]
while pq:
    time, curr = heapq.heappop(pq)
    
    if dist[curr] < time:
        continue
    
    for nxt, t in graph[curr]:
        new_time = time + t
        if dist[nxt] > new_time:
            dist[nxt] = new_time
            parent[nxt] = curr
            heapq.heappush(pq, (new_time, nxt))


path = []
p = N
while p != 1:
    path.append((p, parent[p]))
    p = parent[p]

def dijkstra(x, y):
    res = [INF]*(N+1)
    res[1] = 0
    blocked = set([(x, y), (y, x)])
    pq = [(0, 1)]
    while pq:
        time, curr = heapq.heappop(pq)
        
        if res[curr] < time:
            continue
        
        for nxt, t in graph[curr]:
            if (curr, nxt) in blocked:
                continue
            new_time = time + t
            if res[nxt] > new_time:
                res[nxt] = new_time
                heapq.heappush(pq, (new_time, nxt))
    
    if res[N] == INF:
        return INF
    
    return res[N] - dist[N]

answer = 0
for x, y in path:
    delayed = dijkstra(x, y)
    answer = max(answer, delayed)
    if answer == INF:
        break

print(answer if answer != INF else -1)
