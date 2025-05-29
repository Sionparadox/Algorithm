import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
nextNode = [[] for _ in range(N)]
visited = [False]*N
for _ in range(M):
    s, e = map(int, input().split())
    nextNode[s-1].append(e-1)

queue = deque()
queue.append((0, 0))
answer = -1
while queue:
    now, dist = queue.popleft()
    if now == N-1: 
        answer = dist
        break
    for next in nextNode[now]:
        if not visited[next]:
            visited[next] = True
            queue.append((next, dist+1))

print(answer)