import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
indegree = [0]*N
graph = [[] for _ in range(N)]
time = [0]*N

queue = deque()
answer = [0]*N

for i in range(N):
    arr = list(map(int, input().split()))
    time[i] = arr[0]
    for j in range(1, len(arr)-1):
        indegree[i] += 1
        graph[arr[j]-1].append(i)
    if indegree[i] == 0:
        queue.append(i)
        answer[i] = time[i]

while queue:
    now = queue.popleft()
    
    for next in graph[now]:
        answer[next] = max(answer[next], answer[now]+time[next])
        indegree[next] -= 1
        if indegree[next] == 0:
            queue.append(next)

print('\n'.join(map(str, answer)))


