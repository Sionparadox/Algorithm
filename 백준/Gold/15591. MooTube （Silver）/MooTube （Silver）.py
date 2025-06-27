import sys
input = sys.stdin.readline

N, Q = map(int, input().split())

parent = [x for x in range(N+1)]
size = [1]*(N+1)

def find(node):
    if node == parent[node]:
        return node
    parent[node] = find(parent[node])
    return parent[node]

def union(u, v):
    rootU = find(u)
    rootV = find(v)
    if rootU == rootV:
        return
    if size[rootU] < size[rootV]:
        rootU, rootV = rootV, rootU
    parent[rootV] = rootU
    size[rootU] += size[rootV]

graph = []
for _ in range(N-1):
    u, v, w = map(int, input().split())
    graph.append((w, u, v))

graph.sort(reverse=True)
    
question = []
for i in range(Q):
    k, v = map(int, input().split())
    question.append((k, v, i))

question.sort(reverse=True)

answer = [0]*Q
idx = 0
for k, v, i in question:
    while idx<N-1 and graph[idx][0]>=k:
        _, a, b = graph[idx]
        union(a, b)
        idx += 1
    answer[i] += size[find(v)] -1
    
for ans in answer:
    print(ans)   


'''
import sys
from collections import defaultdict, deque
input = sys.stdin.readline

N, Q = map(int, input().split())

graph = defaultdict(list)
for _ in range(N-1):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

def BFS(k, v):
    visited = [False]*(N+1)
    visited[v] = True
    queue = deque([v])
    res = 0
    while queue:
        now = queue.popleft()
        
        for nxt, val in graph[now]:
            if not visited[nxt] and val >= k:
                visited[nxt] = True
                queue.append(nxt)
                res += 1
    return res

for _ in range(Q):
    k, v = map(int, input().split())
    print(BFS(k, v))

'''  