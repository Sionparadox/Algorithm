import sys
from collections import deque
input = sys.stdin.readline
INF = float('inf')

N, P = map(int, input().split())
L = N*2
graph = [[] for _ in range(L)]
capacity = [[0]*L for _ in range(L)]
flow = [[0]*L for _ in range(L)]
parent = [-1]*L

for i in range(N):
    if i in (0, 1):
        capacity[i][i+N] = INF
    else:
        capacity[i][i+N] = 1
        
    graph[i].append(i+N)
    graph[i+N].append(i)
        
for _ in range(P):
    s, e = map(int, input().split())
    s, e = s-1, e-1
    graph[s+N].append(e)
    graph[e].append(s+N)
    graph[e+N].append(s)
    graph[s].append(e+N)
    capacity[s+N][e] = 1
    capacity[e+N][s] = 1

def BFS(source, sink):
    visited = [False]*L
    queue = deque([source])
    visited[source] = True
    while queue:
        curr = queue.popleft()
        for nxt in graph[curr]:
            if visited[nxt]: continue
            if capacity[curr][nxt] > flow[curr][nxt]:
                visited[nxt] = True
                queue.append(nxt)
                parent[nxt] = curr
                if nxt == sink:
                    return True
    return False

source, sink = N, 1
max_flow = 0
while True:
    if not BFS(source, sink):
        break
    
    u = sink
    while u != source:
        flow[parent[u]][u] += 1
        flow[u][parent[u]] -= 1
        u = parent[u]
    
    max_flow += 1

print(max_flow)