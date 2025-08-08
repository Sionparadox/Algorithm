import sys
from collections import deque
input = sys.stdin.readline

board = [list(input().strip()) for _ in range(8)]
walls = set()
for r in range(8):
    for c in range(8):
        if board[r][c] == '#':
            walls.add((r, c))

directions = [(1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (0, 0)]
queue = deque([(7, 0)])

def move_walls(walls):
    new_walls = set()
    for r, c in walls:
        if r == 7:
            continue
        new_walls.add((r+1, c))
    return new_walls

while queue:
    L = len(queue)
    visited = [[False]*8 for _ in range(8)]
    for _ in range(L):
        r, c = queue.popleft()
        if (r, c) in walls:
            continue
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if nr<0 or nr>=8 or nc<0 or nc>=8:
                continue
            if (nr, nc) in walls or visited[nr][nc]:
                continue
            if nr == 0 and nc == 7:
                print(1)
                exit(0)
            visited[nr][nc] = True
            queue.append((nr, nc))
            
    walls = move_walls(walls)

print(0)


'''
레벨링 BFS사용
한 레벨마다 visited초기화
이동 후 벽확인.
'''