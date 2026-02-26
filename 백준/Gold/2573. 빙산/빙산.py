import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def BFS(r, c):
    queue = deque([(r, c)])
    visited[r][c] = True
    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if nr<0 or nr>=R or nc<0 or nc>=C:
                continue
            if visited[nr][nc]:
                continue
            if board[nr][nc] == 0:
                melted[r][c] += 1
            else:
                visited[nr][nc] = True
                queue.append((nr, nc))

answer = 0
while True:
    cnt = 0
    melted = [[0]*C for _ in range(R)]
    visited = [[False]*C for _ in range(R)]
    
    for r in range(R):
        for c in range(C):
            if not visited[r][c] and board[r][c]>0:
                BFS(r, c)
                cnt += 1
    
    for r in range(R):
        for c in range(C):
            board[r][c] = max(0, board[r][c] - melted[r][c])
    
    if cnt == 0:
        print(0)
        break
    if cnt >= 2:
        print(answer)
        break
    
    answer += 1
