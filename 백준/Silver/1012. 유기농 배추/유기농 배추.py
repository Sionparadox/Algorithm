import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
def BFS(i, j):
    queue = deque()
    queue.append((i, j))
    
    while queue:
        r, c = queue.popleft()
        
        for dr, dc in directions:
            nr = r+dr
            nc = c+dc
            if nr<0 or nr>=N or nc<0 or nc>=M:
                continue
            if board[nr][nc] == 1:
                queue.append((nr, nc))
                board[nr][nc] = 0

for _ in range(T):
    M, N, K = map(int, input().split())
    board = [[0]*M for _ in range(N)]
    answer = 0

    for _ in range(K):
        x, y = map(int, input().split())
        board[y][x] = 1
    
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                BFS(i,j)
                answer += 1  
    print(answer)