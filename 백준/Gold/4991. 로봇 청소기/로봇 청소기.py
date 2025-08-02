import sys
from collections import deque
input = sys.stdin.readline
INF = float('inf')
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def BFS(r, c, board, dist):
    R = len(board)
    C = len(board[0])
    k = board[r][c]
    queue = deque([(r, c, 0)])
    visited = [[False]*C for _ in range(R)]
    visited[r][c] = True
    dist[k][k] = 0
    while queue:
        r, c, d = queue.popleft()
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if nr<0 or nr>=R or nc<0 or nc>=C:
                continue
            if board[nr][nc] == -2 or visited[nr][nc]:
                continue
            if board[nr][nc] >= 0:
                idx = board[nr][nc]
                dist[k][idx] = d+1
            
            visited[nr][nc] = True
            queue.append((nr, nc, d+1))

def solve(R, C, room):
    board = [[-1]*C for _ in range(R)]
    pos = []
    idx = 1
    for r in range(R):
        for c in range(C):
            if room[r][c] == 'o':
                pos.append((r, c))
                board[r][c] = 0
            elif room[r][c] == '*':
                pos.append((r, c))
                board[r][c] = idx
                idx += 1
            elif room[r][c] == 'x':
                board[r][c] = -2
    
    dist = [[INF]*idx for _ in range(idx)]
    for r, c in pos:
        BFS(r, c, board, dist)
    
    if max(max(row) for row in dist) == INF:
        return -1
    
    dp = [[INF]*idx for _ in range(1<<idx)]
    dp[0][0] = 0
    for mask in range(1<<idx):
        for i in range(idx):
            if dp[mask][i] == INF:
                continue
            for j in range(idx):
                if mask | (1<<j) != mask:
                    dp[mask|(1<<j)][j] = min(dp[mask|(1<<j)][j], dp[mask][i]+dist[i][j])
    
    return min(dp[(1<<idx)-1])
    

while True:
    C, R = map(int, input().split())
    if R == 0 and C == 0:
        break
    room = [list(input().strip()) for _ in range(R)]
    print(solve(R, C, room))

'''
BFS로 초기 위치 및 모든 더러운 칸의 위치간 거리를 계산
이후 외판원문제 처럼 최소거리 구하기
dp[mask][i] : mask의 방문 경로로 i번째 노드에 도착했을 때 최소거리
dp[mask | (1<<i)][i] = min(dp[mask|(1<<i)][i], dp[mask][k] + dist[k][i])
'''                