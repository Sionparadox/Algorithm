import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
graph = defaultdict(list)
for _ in range(N-1):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

K = 0
while (1<<K) <= N:
    K += 1

arr = [[-1]*(N+1) for _ in range(K)]
cost = [0]*(N+1)
depth = [0]*(N+1)
def DFS(node, parent):
    for child, w in graph[node]:
        if child != parent:
            arr[0][child] = node
            depth[child] = depth[node]+1
            cost[child] = cost[node]+w
            DFS(child, node)

DFS(1, -1)
for i in range(1, K):
    for j in range(1, N+1):
        if arr[i-1][j] != -1:
            arr[i][j] = arr[i-1][arr[i-1][j]]
            
def get_lca(u, v):
    if depth[u] < depth[v]:
        u, v = v, u
    
    for i in range(K-1, -1, -1):
        if (depth[u]-depth[v]) >= 2**i:
            u = arr[i][u]
    
    if u == v:
        return u
    
    for i in range(K-1, -1, -1):
        if arr[i][u] != arr[i][v]:
            u = arr[i][u]
            v = arr[i][v]
    
    return arr[0][u]


def get_cost(s, e):
    lca = get_lca(s, e)
    return cost[s]+cost[e]-cost[lca]*2

def get_node(s, e, t):
    lca = get_lca(s, e)
    d = depth[s]-depth[lca]+1
    res = s
    if t<=d:
        t -= 1
    else:
        res = e
        t -= d
        t = depth[e]-depth[lca]-t
    
    for i in range(K-1, -1, -1):
        if t & (1<<i):
            res = arr[i][res]
    return res


M = int(input())
for _ in range(M):
    nums = list(map(int, input().split()))
    if nums[0] == 1:
        print(get_cost(nums[1], nums[2]))
    else:
        print(get_node(nums[1], nums[2], nums[3]))

'''
희소배열 활용
거리 : 루트에서 부터 노드까지 거리를 저장해서 LCA를 구해 거리 계산 d1+d2 - 2*d(lca)
노드 : 노드에서 LCA까지 거리를 구해 시작에서 셀지 끝에서 셀지 결정. 거리도 수정.
 -> 이후 K-1부터 내려가며 t번째 노드 구함. 
'''