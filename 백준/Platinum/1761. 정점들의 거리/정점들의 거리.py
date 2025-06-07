import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

parent = [[-1]*(N+1) for _ in range(17)]
depth = [0]*(N+1)
dist = [0]*(N+1)

def dfs(u, p):
    for v, w in graph[u]:
        if v == p:
            continue
        depth[v] = depth[u]+1
        dist[v] = dist[u]+w
        parent[0][v] = u
        dfs(v, u)

dfs(1, -1)      

for i in range(1, 16):
    for j in range(1, N+1):
        if parent[i-1][j] == -1:
            continue
        parent[i][j] = parent[i-1][parent[i-1][j]]

def LCA(u, v):
    # u의 depth가 더 깊게
    if depth[u] < depth[v]:
        u, v = v, u
    
    #u와 v의 depth를 같게 조정
    for i in range(16, -1, -1):
        if parent[i][u] != -1 and depth[parent[i][u]] >= depth[v]:
            u = parent[i][u]
    
    if u == v:
        return u
    
    #u와 v의 부모가 같아질때까지 탐색 
    for i in range(16, -1, -1):
        if parent[i][u] != -1 and parent[i][u] != parent[i][v]:
            u = parent[i][u]
            v = parent[i][v]
    
    return parent[0][u]

M = int(input())
for _ in range(M):
    s, e = map(int, input().split())
    p = LCA(s, e)
    print(dist[s]+dist[e]-2*dist[p])

'''
노드 a,b사이에 거리 : 루트에서 a까지 거리 + 루트에서 b까지 거리 - 둘이 겹치는 경로(최소 공통 조상: LCA)
부모를 찾는 과정이 엄청 길어질 수 있음 << 희소배열로 최적화 (2**16 = 65536)
parent[i][j] : j노드의 2**i번째 부모
parent[i][j] = parent[i-1][parent[i-1][j]]
ex) parent[1][2](2번 노드의 2번째 부모) = parent[0][parent[0][2]](2번 노드의 첫번째 부모의 첫번째 부모)
ex) parent[3][4](4번 노드의 8번째 부모) = parent[2][parent[2][4]](4번 노드의 4번째 부모의 4번째 부모)

어떤 노드도 루트노드가 될 수 있음. -> 1을 임의로 루트로 설정.
dfs로 돌며 depth, dist, parent갱신

'''