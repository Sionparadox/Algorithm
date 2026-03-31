import sys
from collections import deque
input = sys.stdin.readline
INF = float('inf')


N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v, d = map(int, input().split())
    graph[u].append((v, d))
    graph[v].append((u, d))

queue = deque([1])
visited = [False]*(N+1)
visited[1] = True
depth = [0]*(N+1)

LOG = N.bit_length()
parent = [[0]*(N+1) for _ in range(LOG)]
min_dist = [[INF]*(N+1) for _ in range(LOG)]
max_dist = [[0]*(N+1) for _ in range(LOG)]

while queue:
    curr = queue.popleft()
    for nxt, dist in graph[curr]:
        if visited[nxt]:
            continue
        visited[nxt] = True
        queue.append((nxt))
        
        depth[nxt] = depth[curr]+1
        parent[0][nxt] = curr
        min_dist[0][nxt] = dist
        max_dist[0][nxt] = dist

for k in range(1, LOG):
    for i in range(1, N+1):
        node = parent[k-1][i]
        
        parent[k][i] = parent[k-1][node]
        min_dist[k][i] = min(min_dist[k-1][i], min_dist[k-1][node])
        max_dist[k][i] = max(max_dist[k-1][i], max_dist[k-1][node])


def lca(u, v):
    if depth[u] > depth[v]:
        u, v = v, u
    
    min_res = INF
    max_res = 0
    
    diff = depth[v] - depth[u]
    for k in range(LOG):
        if diff & (1<<k):
            min_res = min(min_res, min_dist[k][v])
            max_res = max(max_res, max_dist[k][v])
            v = parent[k][v]
    
    if u == v:
        return min_res, max_res
    
    for k in range(LOG-1, -1, -1):
        if parent[k][u] != parent[k][v]:
            min_res = min(min_res, min_dist[k][u], min_dist[k][v])
            max_res = max(max_res, max_dist[k][u], max_dist[k][v])
            u, v = parent[k][u], parent[k][v]
    
    min_res = min(min_res, min_dist[0][u], min_dist[0][v])
    max_res = max(max_res, max_dist[0][u], max_dist[0][v])
    return min_res, max_res

K = int(input())
for _ in range(K):
    u, v = map(int, input().split())
    print(*lca(u, v))




'''
트리 형태
LCA찾기 (희소배열)
찾는 과정에서 최소거리, 최대거리를 추적할 수 있어야함

'''