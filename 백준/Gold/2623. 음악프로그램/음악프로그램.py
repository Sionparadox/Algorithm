import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
indegree = [0]*(N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    order = list(map(int, input().split()))
    for i in range(1, order[0]):
        graph[order[i]].append(order[i+1])
        indegree[order[i+1]] += 1

queue = deque()
for i in range(1,N+1):
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

if len(answer) == N:
    print('\n'.join(map(str, answer)))
else :
    print(0)
