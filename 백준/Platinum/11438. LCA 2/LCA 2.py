import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N)]
for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

L = 1
while 2**L < N:
    L += 1
parent = [[-1]*N for _ in range(L)]
depth = [0]*N

def DFS(node, p):
    for nxt in graph[node]:
        if nxt == p : continue
        parent[0][nxt] = node
        depth[nxt] = depth[node]+1
        DFS(nxt, node)

DFS(0, -1)

for step in range(1, L):
    for i in range(N):
        if parent[step-1][i] != -1:
            parent[step][i] = parent[step-1][parent[step-1][i]]

M = int(input())

def LCA(u, v):
    if depth[u] < depth[v]:
        u, v = v, u

    for i in range(L-1, -1, -1):
        if depth[u] - depth[v] >= 2**i:
            u = parent[i][u]

    if u == v:
        return u
    
    for i in range(L-1, -1, -1):
        if parent[i][u] != parent[i][v]:
            u = parent[i][u]
            v = parent[i][v]
    
    return parent[0][u]

for _ in range(M):
    u, v = map(int, input().split())
    print(LCA(u-1, v-1)+1)




'''
부모를 기록해서 희소배열로 탐색

1
2 3
4 5 6  / 7 8
9 10 / 11 12 / / 13 14
/ 15

'''