import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

MAX = max(N,K*2)
visited = [False]*(MAX+1)

queue = deque([(N,0)])
visited[N] = True

while queue:
    pos, cnt = queue.popleft()
    if pos == K:
        print(cnt)
        break
    for np in [pos-1, pos+1, pos*2]:
        if np<0 or np>MAX:
            continue
        if visited[np]:
            continue
        visited[np] = True
        queue.append((np, cnt+1))

