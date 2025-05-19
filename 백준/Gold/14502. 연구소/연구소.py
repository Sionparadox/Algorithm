import sys
from itertools import combinations
from collections import deque
import copy
input = sys.stdin.readline

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
empties = []
viruses = []
for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            empties.append((i,j))
        if lab[i][j] == 2:
            viruses.append((i,j))

directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
def simulate(board):
    queue = deque(viruses)
    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr = r+dr
            nc = c+dc
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            if board[nr][nc] == 0:
                board[nr][nc] = 2
                queue.append((nr, nc))
    return sum(row.count(0) for row in board)

answer = 0
for walls in combinations(empties,3):
    simulationLab = copy.deepcopy(lab)
    for r, c in walls:
        simulationLab[r][c] = 1
    answer = max(answer, simulate(simulationLab))

print(answer)
    
    