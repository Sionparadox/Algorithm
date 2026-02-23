import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def BFS(r, c):
    queue = deque([(r, c)])
    visited[r][c] = True
    size = 0
    while queue:
        r, c = queue.popleft()
        size += 1
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if 0>nr or N<=nr or 0>nc or M<=nc:
                continue
            if visited[nr][nc] or board[nr][nc] == 0:
                continue
            visited[nr][nc] = True
            queue.append((nr, nc))
    return size

cnt = 0
area = 0
for r in range(N):
    for c in range(M):
        if board[r][c] == 1 and not visited[r][c]:
            cnt += 1
            area = max(area, BFS(r, c))
            
print(cnt)
print(area)
