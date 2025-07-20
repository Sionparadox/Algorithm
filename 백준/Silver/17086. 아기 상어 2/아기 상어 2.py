import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

queue = deque()
for r in range(N):
    for c in range(M):
        if board[r][c] == 1:
            queue.append((r, c))

directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
answer = 0
while queue:
    L = len(queue)
    for _ in range(L):
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if nr<0 or nr>=N or nc<0 or nc>=M:
                continue
            if board[nr][nc] != 0:
                continue
            board[nr][nc] = board[r][c] + 1
            queue.append((nr, nc))
            answer = board[nr][nc]

print(answer -1)