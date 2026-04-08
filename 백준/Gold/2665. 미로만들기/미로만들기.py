import sys
from collections import deque
input = sys.stdin.readline
INF = float('inf')

N = int(input())
board = [list(map(int, list(input().strip()))) for _ in range(N)]

visited = [[INF]*N for _ in range(N)]
visited[0][0] = 0
queue = deque([(0, 0)])

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
while queue:
    r, c = queue.popleft()
    
    for dr, dc in directions:
        nr, nc = r+dr, c+dc
        if nr<0 or nr>=N or nc<0 or nc>=N:
            continue
        ncnt = visited[r][c] + 1 - board[nr][nc]
        if visited[nr][nc] <= ncnt:
            continue
        visited[nr][nc] = ncnt
        queue.append((nr, nc))

print(visited[N-1][N-1])