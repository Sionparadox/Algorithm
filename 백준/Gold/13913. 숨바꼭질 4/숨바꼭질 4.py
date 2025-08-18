import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
MAX = 100001
prev = [-1]*MAX
visited = [-1]*MAX

queue = deque([N])
visited[N] = 0

while queue:
    pos = queue.popleft()
    if pos == K:
        break
    for nxt in (pos-1, pos+1, pos*2):
        if 0 <= nxt < MAX and visited[nxt] == -1:
            visited[nxt] = visited[pos]+1
            prev[nxt] = pos
            queue.append(nxt)

path = []
now = K
while now != -1:
    path.append(now)
    now = prev[now]

path.reverse()
print(len(path)-1)
print(*path)