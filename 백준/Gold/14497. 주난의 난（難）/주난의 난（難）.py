import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
sr, sc, er, ec = map(lambda x:int(x)-1, input().split())
board = [list(input().strip()) for _ in range(N)]


visited = [[-1]*M for _ in range(N)]
visited[sr][sc] = 1
queue = deque([(sr, sc)])

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
while queue:
    r, c = queue.popleft()
    
    for dr, dc in directions:
        nr, nc = r+dr, c+dc
        if nr<0 or nr>=N or nc<0 or nc>=M:
            continue
        if visited[nr][nc] != -1:
            continue
        
        if board[nr][nc] == '#':
            print(visited[r][c])
            exit()
        if board[nr][nc] == '0':
            visited[nr][nc] = visited[r][c]
            queue.appendleft((nr, nc))
        else:
            visited[nr][nc] = visited[r][c]+1
            queue.append((nr, nc))
