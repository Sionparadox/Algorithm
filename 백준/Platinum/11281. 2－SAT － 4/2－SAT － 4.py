import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
def trans_idx(i):
    if i>0: return i-1
    else: return -i-1+N

graph = [[] for _ in range(2*N)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[trans_idx(-u)].append(trans_idx(v))
    graph[trans_idx(-v)].append(trans_idx(u))

labels = [0]*(2*N)
label = 0
visited = [False]*(2*N)
stack = []
groups = []
group_id = [-1]*(2*N)
group_num = 0
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
        group = []
        while stack:
            cur = stack.pop()
            visited[cur] = False
            group.append(cur)
            group_id[cur] = group_num
            if cur == node:
                break
        groups.append(group)
        group_num += 1
    return parent

for i in range(2*N):
    if not labels[i]:
        DFS(i)

answer = 1
for i in range(N):
    if group_id[i] == group_id[i+N]:
        answer = 0
        break

if answer == 0:
    print(answer)
    exit(0)

G = len(groups)
indegree = [0]*G
for node in range(2*N):
    for nxt in graph[node]:
        if group_id[node] != group_id[nxt]:
            indegree[group_id[nxt]] += 1

queue = deque()
for i in range(G):
    if indegree[i] == 0:
        queue.append(i)

order = []
while queue:
    cur = queue.popleft()
    order.append(cur)
    
    for node in groups[cur]:
        for nxt in graph[node]:
            nid = group_id[nxt]
            if cur == nid: continue
            indegree[nid] -= 1
            if indegree[nid] == 0:
                queue.append(nid)
     
group_value = [-1]*G           
for g in order:
    if group_value[g] == -1:
        group_value[g] = 0
        for node in groups[g]:
            rn = node+N if node < N else node-N
            group_value[group_id[rn]] = 1

value = [0]*N
for i in range(N):
    if group_value[group_id[i]]:
        value[i] = 1
        
print(answer)
print(*value)