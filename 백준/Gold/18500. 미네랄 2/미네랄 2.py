import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
cave = [list(input().strip()) for _ in range(R)]
N = int(input())
heights = list(map(int, input().split()))

directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def throw(height, dir):
    height = R-height
    if dir == 1:
        for c in range(C):
            if cave[height][c] == 'x':
                cave[height][c] = '.'
                return height, c
    else:
        for c in range(C-1, -1, -1):
            if cave[height][c] == 'x':
                cave[height][c] = '.'
                return height, c
    return None, None

def BFS(r, c):
    queue = deque([(r, c)])
    visited[r][c] = True
    res = [(r, c)]
    isBottom = (r == R-1)
    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if 0<=nr<R and 0<=nc<C and not visited[nr][nc] and cave[nr][nc] == 'x':
                visited[nr][nc] = True
                queue.append((nr, nc))
                res.append((nr, nc))
                if nr == R-1:
                    isBottom = True
    return res, isBottom

def fall(cluster):
    if not cluster:
        return
    for r, c in cluster:
        cave[r][c] = '.'
    
    max_drop = R
    for r, c in cluster:
        drop_dist = 0
        while r + drop_dist + 1 < R and cave[r + drop_dist + 1][c] == '.':
            drop_dist += 1
        max_drop = min(max_drop, drop_dist)
    
    for r, c in cluster:
        cave[r + max_drop][c] = 'x'

for i in range(N):
    height = heights[i]
    dir = 1 if i%2==0 else -1
    br, bc = throw(height, dir)
    if br is None:
        continue
    visited = [[False]*C for _ in range(R)]
    for dr, dc in directions:
        nr, nc = br+dr, bc+dc
        if 0<=nr<R and 0<=nc<C and not visited[nr][nc] and cave[nr][nc] == 'x':
            cluster, isBottom = BFS(nr, nc)
            if cluster and not isBottom:
                fall(cluster)
                break

print('\n'.join([''.join(row) for row in cave]))