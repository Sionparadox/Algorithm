import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def DFS(node):
    global label, group_num
    label += 1
    labels[node] = label
    parent = label
    stack.append(node)
    visited[node] = True
    
    for nxt in graph[node]:
        if labels[nxt] == 0:
            parent = min(parent, DFS(nxt))
        elif visited[nxt]:
            parent = min(parent, labels[nxt])
    
    if parent == labels[node]:
        res = []
        while stack:
            cur = stack.pop()
            group_id[cur] = group_num
            res.append(cur)
            visited[cur] = False
            if node == cur:
                break
        groups.append(res)
        group_num += 1
    
    return parent
    

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
    labels = [0]*(N+1)
    visited = [False]*(N+1)
    stack = []
    groups = []
    group_id = [-1]*(N+1)
    label = group_num = 0
    for i in range(1, N+1):
        if labels[i] == 0:
            p = DFS(i)
    
    G = len(groups)
    indegree = [0]*G
    for node in range(1, N+1):
        for nxt in graph[node]:
            if group_id[node] != group_id[nxt]:
                indegree[group_id[nxt]] += 1
    
    answer = 0
    for i in range(G):
        if indegree[i] == 0:
            answer += 1
    
    print(answer)