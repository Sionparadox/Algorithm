import sys, heapq
input = sys.stdin.readline
INF = float('inf')

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, cost = map(int, input().split())
    graph[u].append((v, cost))
    graph[v].append((u, cost))

dist = [INF]*(N+1)
parent = list(range(N+1))
dist[1] = 0
pq = []
heapq.heappush(pq, (0, 1))

while pq:
    cost, curr = heapq.heappop(pq)
    
    if dist[curr] < cost:
        continue
    
    for nxt, ncost in graph[curr]:
        new_cost = ncost+cost
        if dist[nxt] > new_cost:
            dist[nxt] = new_cost
            parent[nxt] = curr
            heapq.heappush(pq, (new_cost, nxt))

print(N-1)
for idx in range(2, N+1):
    print(idx, parent[idx])

            
'''
모든 노드를 연결해야 하니 개수 최소는 무조건 N-1
각각의 parent - idx를 연결하면 정답
'''