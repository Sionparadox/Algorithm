import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visitBoard = [[False]*N for _ in range(N)]
directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def BFS(r, c):
    color = board[r][c]
    blocks = [(r, c)]
    rainbow = 0
    queue = deque([(r, c)])
    visited = set([(r, c)])
    visitBoard[r][c] = True
    
    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if nr<0 or nr>=N or nc<0 or nc>=N:
                continue
            if (nr, nc) in visited or board[nr][nc] not in (0, color):
                continue
            queue.append((nr, nc))
            blocks.append((nr, nc))
            visited.add((nr, nc))
            if board[nr][nc] == 0:
                rainbow += 1
            else:
                visitBoard[nr][nc] = True
    
    return (len(blocks), rainbow, blocks)

def fall():
    for c in range(N):
        for r in range(N-1, -1, -1):
            if board[r][c] >= 0:
                for i in range(r, N):
                    if i == N-1 or board[i+1][c] != -2:
                        board[r][c], board[i][c] = board[i][c], board[r][c]
                        break


def rotate():
    return [list(row) for row in zip(*board)][::-1]


answer = 0
while True:
    visitBoard = [[False]*N for _ in range(N)]
    groups = []
    cnt = 0
    for r in range(N):
        for c in range(N):
            if board[r][c] > 0 and not visitBoard[r][c]:
                group = BFS(r, c)
                if group[0] > 1:                
                    groups.append(group)
                    
    if len(groups) == 0:
        break
    
    groups.sort(reverse=True)
    blockGroup = groups[0]
    answer += blockGroup[0]**2
    for r, c in blockGroup[2]:
        board[r][c] = -2
    fall()
    board[:] = rotate()
    fall()

print(answer)