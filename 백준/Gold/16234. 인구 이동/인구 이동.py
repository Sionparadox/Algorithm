import sys
from collections import deque
input = sys.stdin.readline

N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
def BFS(r, c):
    union = [(r, c)]
    total = board[r][c]
    queue = deque()
    queue.append((r, c))
    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if nr < 0 or nr >= N or nc < 0 or nc >= N or (nr, nc) in visited:
                continue
            if L <= abs(board[r][c]-board[nr][nc]) <= R:
                union.append((nr, nc))
                total += board[nr][nc]
                queue.append((nr, nc))
                visited.add((nr, nc))
    if len(union) == 1:
        return False
    
    for i, j in union:
        board[i][j] = total//len(union)
    
    return True
    
for t in range(2000):
    visited = set()
    isMove = False
    for i in range(N):
        for j in range(N):
            if (i, j) not in visited:
                visited.add((i, j))
                isMove |= BFS(i, j)
    if not isMove:
        break
print(t)