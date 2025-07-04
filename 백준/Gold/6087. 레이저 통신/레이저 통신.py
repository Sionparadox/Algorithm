import sys
import heapq
input = sys.stdin.readline

W, H = map(int, input().split())
room = [list(input().strip()) for _ in range(H)]
pos = []

for i in range(H):
    for j in range(W):
        if room[i][j] == 'C':
            pos.append((i, j))

start = pos[0]
end = pos[1]
dp = [[[float('inf')]*4 for _ in range(W)] for _ in range(H)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

pq = []
for d in range(4):
    dp[start[0]][start[1]][d] = 0
    heapq.heappush(pq, (0, start[0], start[1], d))

while pq:
    val, r, c, dir = heapq.heappop(pq)
    if dp[r][c][dir] < val:
        continue
    
    for d in range(4):
        dr, dc = directions[d]
        nr, nc = r+dr, c+dc
        if nr<0 or nr>=H or nc<0 or nc>=W:
            continue
        if room[nr][nc] == '*':
            continue
        
        new_val = val + (dir != d)
        if dp[nr][nc][d] > new_val:
            dp[nr][nc][d] = new_val
            heapq.heappush(pq, (new_val, nr, nc, d))

print(min(dp[end[0]][end[1]]))  