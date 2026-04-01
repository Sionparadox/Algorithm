import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

LOG = N.bit_length()
queue = deque([1])
parent = [[0]*(N+1) for _ in range(LOG)]
depth = [-1]*(N+1)
depth[1] = 0

while queue:
    curr = queue.popleft()
    
    for nxt in graph[curr]:
        if depth[nxt] != -1:
            continue
        parent[0][nxt] = curr
        depth[nxt] = depth[curr]+1
        queue.append(nxt)

for k in range(1, LOG):
    for i in range(1, N+1):
        parent[k][i] = parent[k-1][parent[k-1][i]]

def lca(u, v):
    if depth[u] > depth[v]:
        u, v = v, u
    
    diff = depth[v] - depth[u]
    for k in range(LOG):
        if diff & (1<<k):
            v = parent[k][v]
    
    if u == v:
        return u
    
    for k in range(LOG-1, -1, -1):
        if parent[k][u] != parent[k][v]:
            u = parent[k][u]
            v = parent[k][v]
    
    return parent[0][u]

M = int(input())
for _ in range(M):
    u, v = map(int, input().split())
    print(lca(u, v))
