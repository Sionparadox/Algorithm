import sys, heapq
input = sys.stdin.readline
INF = float('inf')

C, R = map(int, input().split())
board = [list(map(int, list(input().rstrip()))) for _ in range(R)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

visited = [[INF]*C for _ in range(R)]
visited[0][0] = 0
pq = [(0, 0, 0)]

while pq:
    cnt, r, c = heapq.heappop(pq)
    if cnt > visited[r][c]:
        continue
    for dr, dc in directions:
        nr, nc, ncnt = r+dr, c+dc, cnt
        if nr<0 or nr>=R or nc<0 or nc>=C:
            continue            
        if board[nr][nc] == 1:
            ncnt += 1
        if visited[nr][nc] <= ncnt:
            continue
        visited[nr][nc] = ncnt
        heapq.heappush(pq, (ncnt, nr, nc))

print(visited[R-1][C-1])