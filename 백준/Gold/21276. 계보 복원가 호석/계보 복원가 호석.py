import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
names = list(input().split())
names.sort()
nameIdx = {}
for i in range(N):
    nameIdx[names[i]] = i

M = int(input())
indegree = [0]*N
graph = [[] for _ in range(N)]
for _ in range(M):
    child, parent = input().split()
    c, p = nameIdx[child], nameIdx[parent]
    graph[p].append(c)
    indegree[c] += 1

root = []
children = [[] for _ in range(N)]
queue = deque()
for i in range(N):
    if indegree[i] == 0:
        root.append(names[i])
        queue.append(i)

while queue:
    curr = queue.popleft()
    for nxt in graph[curr]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            children[curr].append(names[nxt])
            queue.append(nxt)

print(len(root))
print(*root)
for i in range(N):
    print(names[i], len(children[i]), *sorted(children[i]))
