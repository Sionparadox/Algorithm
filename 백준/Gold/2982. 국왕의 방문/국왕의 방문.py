import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
A, B, K, G = map(int, input().split())
graph = [[] for _ in range(N+1)]

route = list(map(int, input().split()))

for _ in range(M):
    u, v, t = map(int, input().split())
    graph[u].append((v, t))
    graph[v].append((u, t))

wait = {}
time = 0
for i in range(G-1):
    u, v  = route[i], route[i+1]
    for next, t in graph[u]:
        if next == v:
            break
    
    wait[(u,v)] = (time, time+t)
    wait[(v,u)] = (time, time+t)
    time += t

dist = [float('inf')]*(N+1)
dist[A] = K
pq = []
heapq.heappush(pq, (K, A))

while pq:
    now, curr = heapq.heappop(pq)
    if dist[curr] < now:
        continue
    for next, t in graph[curr]:
        nt = now+t
        s, e = wait.get((curr, next), (-1, -1))
        if s != -1 and s <= now < e:
            nt = e+t
        if dist[next] > nt:
            dist[next] = nt
            heapq.heappush(pq, (nt, next))

print(dist[B]-K)

