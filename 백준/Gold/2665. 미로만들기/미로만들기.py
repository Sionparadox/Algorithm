import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
board = [list(map(int, list(input().strip()))) for _ in range(N)]

visited = [[-1]*N for _ in range(N)]
visited[0][0] = 0
queue = deque([(0, 0)])

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
while queue:
    r, c = queue.popleft()
    if r == N-1 and c == N-1:
        print(visited[r][c])
        break
    
    for dr, dc in directions:
        nr, nc = r+dr, c+dc
        if nr<0 or nr>=N or nc<0 or nc>=N:
            continue
        if visited[nr][nc] != -1:
            continue
        
        if board[nr][nc] == 1:
            visited[nr][nc] = visited[r][c]
            queue.appendleft((nr, nc))
        else:
            visited[nr][nc] = visited[r][c] + 1
            queue.append((nr, nc))

