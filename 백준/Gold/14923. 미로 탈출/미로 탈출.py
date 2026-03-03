import sys
from collections import deque
input = sys.stdin.readline
INF = float('inf')

N, M = map(int, input().split())
Hx, Hy = map(int, input().split())
Ex, Ey = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dist = [[[-1]*2 for _ in range(M)] for _ in range(N)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
queue = deque([(Hx-1, Hy-1, 0)])
dist[Hx-1][Hy-1][0] = 0

answer = -1
while queue:
    r, c, t = queue.popleft()
    d = dist[r][c][t]
    if r == Ex-1 and c == Ey-1:
        answer = d
        break

    for dr ,dc in directions:
        nr, nc = r+dr, c+dc
        if nr<0 or nr>=N or nc<0 or nc>=M:
            continue
            
        if board[nr][nc] == 0 and dist[nr][nc][t] == -1:
            dist[nr][nc][t] = d+1
            queue.append((nr, nc, t))
        
        if board[nr][nc] == 1 and t == 0 and dist[nr][nc][1] == -1:
            dist[nr][nc][1] = d+1
            queue.append((nr, nc, 1))
        

print(answer)       

'''
dist[r][c][t]
r,c까지 도착한 거리(t : 벽을 부수고 왔는지 플래그)
'''