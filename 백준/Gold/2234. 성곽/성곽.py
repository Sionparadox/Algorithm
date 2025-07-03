import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(M)]
visited = [[False]*N for _ in range(M)]
directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]

def BFS(r, c):
    visited[r][c] = True
    queue = deque([(r, c)])
    res = [(r, c)]
    while queue:
        r, c = queue.popleft()
        for d in range(4):
            if room[r][c] & (1<<d):
                continue
            dr, dc = directions[d]
            nr, nc = r+dr, c+dc
            if not visited[nr][nc]: 
                visited[nr][nc] = True
                queue.append((nr, nc))
                res.append((nr, nc))
    return res

res = []
for r in range(M):
    for c in range(N):
        if not visited[r][c]:
            res.append(BFS(r, c))

size = [len(arr) for arr in res]
index = [[0]*N for _ in range(M)]

for idx in range(len(res)):
    arr = res[idx]
    for r, c in arr:
        index[r][c] = idx

maxVal = 0
for r in range(M):
    for c in range(N):
        if r != M-1 and index[r][c] != index[r+1][c]:
            maxVal = max(maxVal, size[index[r][c]]+size[index[r+1][c]])
        if c != N-1 and index[r][c] != index[r][c+1]:
            maxVal = max(maxVal, size[index[r][c]]+size[index[r][c+1]])

print(len(res))
print(max(size))
print(maxVal)