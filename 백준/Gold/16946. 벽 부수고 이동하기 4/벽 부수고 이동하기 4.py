import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(N)]
group = [[(-1, -1) for _ in range(M)]for _ in range(N)]
groupDict = {}

directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
def BFS(i, j):
    queue = deque()
    queue.append((i, j))
    group[i][j] = (i,j)
    groupDict[(i,j)] = 1
    while queue:
        r, c = queue.popleft()
        
        for dr, dc in directions:
            nr = r+dr
            nc = c+dc
            if nr<0 or nr >=N or nc < 0 or nc >= M:
                continue
            if board[nr][nc] == 0 and group[nr][nc] == (-1, -1):
                group[nr][nc] = (i, j)
                groupDict[(i,j)] += 1
                queue.append((nr, nc))

for i in range(N):
    for j in range(M):
        if group[i][j] == (-1, -1) and board[i][j] == 0:
            BFS(i, j)

answer = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            candidate = set()
            answer[i][j] = 1
            for dr, dc in directions:
                ni = i+dr
                nj = j+dc
                if 0<=ni<N and 0<=nj<M and board[ni][nj] == 0:
                    candidate.add(group[ni][nj])
            for pos in candidate:
                answer[i][j] += groupDict[pos]
                answer[i][j] %= 10
        else :
            answer[i][j] = 0

print('\n'.join([''.join(map(str, row)) for row in answer]))