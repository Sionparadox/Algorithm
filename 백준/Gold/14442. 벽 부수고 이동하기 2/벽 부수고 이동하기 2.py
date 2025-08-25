import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())
board = [input().strip() for _ in range(N)]
visited = [[[False]*(K+1) for _ in range(M)] for _ in range(N)]
visited[0][0][0] = True
queue = deque([(0, 0, 0, 1)])

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
answer = -1
while queue:
    r, c, k, cnt = queue.popleft()
    
    if r == N-1 and c == M-1:
        answer = cnt
        break
    
    for dr, dc in directions:
        nr, nc, nk = r+dr, c+dc, k
        if nr<0 or nr>=N or nc<0 or nc>=M:
            continue
        if board[nr][nc] == '1':
            nk += 1
        if nk>K or visited[nr][nc][nk]:
            continue
        visited[nr][nc][nk] = True
        queue.append((nr, nc, nk, cnt+1))

print(answer)