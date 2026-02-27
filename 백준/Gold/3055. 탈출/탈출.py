import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
board = [list(input().rstrip()) for _ in range(R)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[False]*C for _ in range(R)]
water_visited = [[False]*C for _ in range(R)]

queue = deque()
water = deque()
for r in range(R):
    for c in range(C):
        if board[r][c] == 'S':
            queue.append((r, c))
            visited[r][c] = True
        if board[r][c] == '*':
            water.append((r, c))
            water_visited[r][c] = True

    
answer = 0

while queue:
    for _ in range(len(water)):
        r, c = water.popleft()
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if nr<0 or nr>=R or nc<0 or nc>=C:
                continue
            if water_visited[nr][nc]:
                continue
            if board[nr][nc] in ('D', 'X'):
                continue
            board[nr][nc] = '*'
            water_visited[nr][nc] = True
            water.append((nr, nc))
    
    for _ in range(len(queue)):
        r, c = queue.popleft()
        if board[r][c] == 'D':
            print(answer)
            exit(0)
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if nr<0 or nr>=R or nc<0 or nc>=C:
                continue
            if visited[nr][nc] or board[nr][nc] in ('*', 'X'):
                continue
            visited[nr][nc] = True
            queue.append((nr, nc))
        
    answer += 1

print('KAKTUS')
'''
물이 퍼짐(1step)
고슴도치가 움직임(1step)
두 BFS를 한 level 안에 진행
'''