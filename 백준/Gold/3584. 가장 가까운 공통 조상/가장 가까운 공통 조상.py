import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def LCA(u, v):
    if depth[u] < depth[v]:
        u, v = v, u
    
    for i in range(K-1, -1, -1):
        if depth[u]-depth[v] >= 2**i:
            u = parent[i][u]
    
    if u == v:
        return u
    
    for i in range(K-1, -1, -1):
        if parent[i][u] != parent[i][v]:
            u = parent[i][u]
            v = parent[i][v]
    
    return parent[0][u]
    
def DFS(node, parent):
    for child in graph[node]:
        if child != parent:
            depth[child] = depth[node]+1
            DFS(child, node)

T = int(input())
for _ in range(T):
    N = int(input())
    K = 0
    while 2**K <= N:
        K += 1
    
    parent = [[-1]*(N+1) for _ in range(K)]
    depth = [0]*(N+1)
    graph = [[] for _ in range(N+1)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        parent[0][b] = a
        graph[a].append(b)
    
    root = 0
    for i in range(1, N+1):
        if parent[0][i] == -1:
            root = i
            break
    
    DFS(root, 0)
    for i in range(1, K):
        for j in range(1, N+1):
            parent[i][j] = parent[i-1][parent[i-1][j]]
    
    U, V = map(int, input().split())
    print(LCA(U, V))