import sys
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

print(answer)

'''
각 변수들 사이 edge로 표현 가능
A or B : not A -> B or not B -> A

서로 연관관계가 있는 변수끼리 묶어서
반드시 False가 나오는 그룹이 하나라도 존재하면 0
아니면 1
'''