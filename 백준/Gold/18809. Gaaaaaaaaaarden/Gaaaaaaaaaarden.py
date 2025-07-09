import sys
from itertools import combinations
from collections import deque
INF = float('inf')
input = sys.stdin.readline

N, M, G, R = map(int, input().split())
garden = [list(map(int, input().split())) for _ in range(N)]
canSeed = []
for r in range(N):
    for c in range(M):
        if garden[r][c] == 2:
            canSeed.append((r, c))

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def BFS(greens, reds):
    visited = [[INF]*M for _ in range(N)]
    queue = deque()
    for r, c in greens:
        queue.append((r, c))
        visited[r][c] = 0
    for r, c in reds:
        queue.append((r, c))
        visited[r][c] = 1
    
    time = 0
    res = 0
    while queue:
        time += 1
        for _ in range(len(queue)):
            r, c = queue.popleft()
            if visited[r][c] == -1:
                continue
            color = visited[r][c] % 2 # 0:green, 1:red
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if nr<0 or nr>=N or nc<0 or nc>=M:
                    continue
                if garden[nr][nc] == 0 or visited[nr][nc] < time*2:
                    continue
                if visited[nr][nc] == 2*time+(1-color):
                    res += 1
                    visited[nr][nc] = -1
                    continue
                if visited[nr][nc] == INF:
                    visited[nr][nc] = 2*time+color
                    queue.append((nr, nc))
                    
    return res

answer = 0
for comb in combinations(canSeed, G+R):
    for greens in combinations(comb, G):
        reds = [pos for pos in comb if pos not in greens]
        answer = max(answer, BFS(greens, reds))
print(answer)