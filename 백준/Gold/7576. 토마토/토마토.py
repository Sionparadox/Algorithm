import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
queue = deque()
for r in range(N):
    for c in range(M):
        if board[r][c] == 1:
            queue.append((r, c))

answer = -1
while queue:
    L = len(queue)
    answer += 1
    for _ in range(L):
        r, c = queue.popleft()
        for dr ,dc in directions:
            nr, nc = r+dr, c+dc
            if nr<0 or nr>=N or nc<0 or nc>=M:
                continue
            if board[nr][nc] == 0:
                board[nr][nc] = 1
                queue.append((nr, nc))


for r in range(N):
    for c in range(M):
        if board[r][c] == 0:
            answer = -1
            break
print(answer)


'''
leveling BFS?

'''