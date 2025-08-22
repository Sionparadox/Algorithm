import sys
from collections import deque
input = sys.stdin.readline
INF = float('inf')

N, M, K = map(int, input().split())
board = [list(map(int, list(input().strip()))) for _ in range(N)]
visited = [[[INF]*M for _ in range(N)] for _ in range(K+1)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


queue = deque([(0, 0, 0)]) #n, m, k
visited[0][0][0] = 1
while queue:
    r, c, k = queue.popleft()
    cnt = visited[k][r][c]
    
    for dr, dc in directions:
        nr, nc, nk, nt = r+dr, c+dc, k, cnt+1
        if nr<0 or nr>=N or nc<0 or nc>=M:
            continue
        if board[nr][nc] == 1:
            if nk == K: continue
            if cnt % 2 == 0:
                nt += 1
            nk += 1
        if visited[nk][nr][nc] <= nt: continue
        visited[nk][nr][nc] = nt
        queue.append((nr, nc, nk))
    
answer = INF
for k in range(K+1):
    answer = min(answer, visited[k][N-1][M-1])
print(answer if answer != INF else -1)
'''
visited[day][k][n][m]
-> 0,0움직임 때문인지 시간초과
visited[k][n][m] 으로 개선
큐에서 cnt를 통해 홀짝으로 밤낮을 구분
'''