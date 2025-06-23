import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
queue = deque()
answer = [[-1]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if board[i][j] == 2:
            queue.append((i, j, 0))
            answer[i][j] = 0
        if board[i][j] == 0:
            answer[i][j] = 0

directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

while queue:
    r, c, k = queue.popleft()
    
    for dr, dc in directions:
        nr, nc = r+dr, c+dc
        if nr<0 or nr>=N or nc<0 or nc>=M:
            continue
        if board[nr][nc] == 1 and answer[nr][nc] == -1:
            answer[nr][nc] = k+1
            queue.append((nr, nc, k+1))
print('\n'.join([' '.join(map(str, arr)) for arr in answer]))