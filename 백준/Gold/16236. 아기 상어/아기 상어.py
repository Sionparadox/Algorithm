import sys
import heapq
from collections import deque
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
shark = (0, 0)
for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            shark = (i, j)
            board[i][j] = 0
            break

size = food = 2
time = 0
directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
def getDistance(endR, endC):
    queue = deque()
    visited = set()
    initR, initC = shark
    queue.append((0, initR, initC))
    visited.add((initR, initC))
    while queue:
        d, r, c = queue.popleft()
        for dr, dc in directions:
            nr = r+dr
            nc = c+dc
            if nr == endR and nc == endC:
                return d+1
            if 0<=nr<N and 0<=nc<N and board[nr][nc] <= size and (nr, nc) not in visited:
                queue.append((d+1, nr, nc))
                visited.add((nr, nc))
    return 0

while True:
    pq = []
    for i in range(N):
        for j in range(N):
            if 0<board[i][j]<size:
                d = getDistance(i,j)
                if d != 0:
                    heapq.heappush(pq, (d, i, j))
    if not pq:
        break
    
    distance, r, c = heapq.heappop(pq)
    time += distance
    shark = (r, c)
    board[r][c] = 0
    food -= 1
    if food == 0:
        size += 1
        food = size

print(time)