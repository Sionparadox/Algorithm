import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
pool = [list(map(int, input().split())) for _ in range(N)]

pq = []
visited = [[False]*M for _ in range(N)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for r in range(N):
    for c in range(M):
        if r == 0 or r == N-1 or c == 0 or c == M-1:
            visited[r][c] = True
            heapq.heappush(pq, (pool[r][c], r, c))

answer = 0
while pq:
    h, r, c = heapq.heappop(pq)
    
    for dr, dc in directions:
        nr, nc = r+dr, c+dc
        if nr<0 or nr >= N or nc <0 or nc >= M:
            continue
        if not visited[nr][nc]:
            visited[nr][nc] = True
            if pool[nr][nc] < h:
                answer += h - pool[nr][nc]
            heapq.heappush(pq, (max(h, pool[nr][nc]), nr, nc))
            
print(answer)