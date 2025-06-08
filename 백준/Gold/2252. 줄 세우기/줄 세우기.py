import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
indegree = [0]*(N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    indegree[e] += 1

queue = deque()
for i in range(1, N+1):
    if indegree[i] == 0:
        queue.append(i)

answer = []
while queue:
    now = queue.popleft()
    answer.append(now)
    
    for next in graph[now]:
        indegree[next] -= 1
        if indegree[next] == 0:
            queue.append(next)

print(' '.join(map(str, answer)))
