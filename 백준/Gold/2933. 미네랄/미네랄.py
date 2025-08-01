import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
cave = [list(input().strip()) for _ in range(R)]
H = int(input())
heights = list(map(int, input().split()))
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def findCluster(r, c):
    res = [(r, c)]
    queue = deque([(r, c)])
    visited[r][c] = True
    bottom = r
    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if nr<0 or nr>=R or nc<0 or nc>=C:
                continue
            if visited[nr][nc] or cave[nr][nc] == '.':
                continue
            visited[nr][nc] = True
            queue.append((nr, nc))
            res.append((nr, nc))
            bottom = max(bottom, nr)
    return res, bottom

def throw(height, d):
    height = R-height
    for c in range(C)[::d]:
        if cave[height][c] == 'x':
            cave[height][c] = '.'
            return height, c
    
    return None, None

def fall(cluster, bottom):
    minDist = R
    for r, c in cluster:
        cave[r][c] = '.'
    for r, c in cluster:
        dist = 0
        while r+dist+1<R and cave[r+dist+1][c] == '.':
            dist += 1
        minDist = min(minDist, dist)
    for r, c in cluster:
        cave[r+minDist][c] = 'x'

d = 1
for height in heights:
    r, c = throw(height, d)
    d *= -1
    if r == None:
        continue
    visited = [[False]*C for _ in range(R)]
    for dr, dc in directions:
        nr, nc = r+dr, c+dc
        if nr<0 or nr>=R or nc<0 or nc>=C:
            continue
        if visited[nr][nc] or cave[nr][nc] == '.':
            continue
        cluster, bottom = findCluster(nr, nc)
        if bottom != R-1:
            fall(cluster, bottom)
            break

print('\n'.join(''.join(row) for row in cave))