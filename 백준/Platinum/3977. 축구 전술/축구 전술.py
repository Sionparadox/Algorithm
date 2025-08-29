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
        if not labels[nxt]:
            parent = min(parent, DFS(nxt))
        elif visited[nxt]:
            parent = min(parent, labels[nxt])
    
    if parent == labels[node]:
        group = []
        while stack:
            cur = stack.pop()
            group_id[cur] = group_num
            group.append(cur)
            visited[cur] = False
            if cur == node:
                break
        groups.append(group)
        group_num += 1
    
    return parent

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
    
    labels = [0]*N
    label = 0
    visited = [False]*N
    groups = []
    group_id = [-1]*N
    group_num = 0
    stack = []
    for i in range(N):
        if not labels[i]:
            DFS(i)
    
    G = len(groups)
    indegree = [0]*G
    for node in range(N):
        for nxt in graph[node]:
            if group_id[node] != group_id[nxt]:
                indegree[group_id[nxt]] += 1
    cnt = 0
    res = []
    for i in range(G):
        if indegree[i] == 0:
            cnt += 1
            res.extend(groups[i])
    if cnt != 1:
        print("Confused")
    else:
        print('\n'.join(map(str, sorted(res))))
    print()
    input()
    