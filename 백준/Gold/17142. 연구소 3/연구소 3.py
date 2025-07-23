import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
virus = set()
empty = 0
for r in range(N):
    for c in range(N):
        if room[r][c] == 2:
            virus.add((r, c))
        if room[r][c] == 0:
            empty += 1

if empty == 0:
    print(0)
    exit(0)

directions =[(0, -1), (0, 1), (-1, 0), (1, 0)]
def BFS(viruses):
    queue = deque(viruses)
    visited = [[False]*N for _ in range(N)]
    for r, c in viruses:
        visited[r][c] = True
    
    filled = 0
    res = 0
    while queue:
        L = len(queue)
        res += 1
        for _ in range(L):
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if nr<0 or nr>=N or nc<0 or nc>=N:
                    continue
                if visited[nr][nc] or room[nr][nc] == 1:
                    continue
                if room[nr][nc] == 0:
                    filled += 1
                visited[nr][nc] = True
                queue.append((nr, nc))
        if filled >= empty:
            return res
    return N**2

answer = N**2
for viruses in combinations(virus, M):
    answer = min(answer, BFS(viruses))

print(answer if answer <N**2 else -1)