import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(R)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def BFS():
    queue = deque([(0, 0)])
    visited = [[False]*C for _ in range(R)]
    visited[0][0] = True
    melt = set()
    
    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if nr<0 or nr>= R or nc<0 or nc>=C:
                continue
            if visited[nr][nc]:
                continue
            if cheese[nr][nc]:
                melt.add((nr, nc))
            else:
                visited[nr][nc] = True
                queue.append((nr, nc))
    
    for r, c in melt:
        cheese[r][c] = 0
            
    return len(melt)


time = 0
piece = sum([sum(row) for row in cheese])
while True:
    cnt = BFS()
    
    time += 1
    piece -= cnt

    if piece <= 0:
        print(time)
        print(cnt)
        break
