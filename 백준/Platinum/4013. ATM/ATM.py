import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u, v = u-1, v-1
    graph[u].append(v)

cash = [int(input()) for _ in range(N)]
S, P = map(int, input().split())
S -= 1
restaurant = set(x-1 for x in list(map(int, input().split())))

visited = [False]*N
labels = [0]*N
label = 0
groups = []
group_id = [-1]*N
group_num = 0
stack = []

def DFS(node):
    global label, group_num
    label += 1
    labels[node] = label
    parent = label
    visited[node] = True
    stack.append(node)
    
    for nxt in graph[node]:
        if not labels[nxt]:
            parent = min(parent, DFS(nxt))
        elif visited[nxt]:
            parent = min(parent, labels[nxt])
    
    if parent == labels[node]:
        group = []
        while stack:
            cur = stack.pop()
            visited[cur] = False
            group_id[cur] = group_num
            group.append(cur)
            if cur == node:
                break
        groups.append(group)
        group_num += 1
    
    return parent

for i in range(N):
    if not labels[i]:
        DFS(i)

G = len(groups)
group_cash = [0]*G
group_rest = [False]*G
for i in range(G):
    for g in groups[i]:
        group_cash[i] += cash[g]
        group_rest[i] |= g in restaurant

indegree = [0]*G
dp = [0]*G
can_visit = [False]*G

for node in range(N):
    for nxt in graph[node]:
        if group_id[node] != group_id[nxt]:
            indegree[group_id[nxt]] += 1

sg = group_id[S]
dp[sg] = group_cash[sg]
can_visit[sg] = True

queue = deque()
for i in range(G):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    cur = queue.popleft()
    
    for node in groups[cur]:
        for nxt in graph[node]:
            ng = group_id[nxt]
            if cur == ng: continue

            indegree[ng] -= 1
            if indegree[ng] == 0:
                queue.append(ng)
            
            if can_visit[cur]:
                if dp[ng] < dp[cur] + group_cash[ng]:
                    dp[ng] = dp[cur] + group_cash[ng]
                can_visit[ng] = True

answer = 0
for i in range(G):
    if group_rest[i] and can_visit[i]:
        answer = max(answer, dp[i])

print(answer)