import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

N, M, D = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
directions = [(0, -1), (-1, 0), (0, 1)]

def findEnemy(r, c, arr):
    queue = deque([(r, c, 1)])
    visited = set([(r, c)])
    while queue:
        r, c, d = queue.popleft()
        if arr[r][c] == 1:
            return (r, c)
        if d == D:
            continue
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if 0<=nr<N and 0<=nc<M and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc, d+1))
    return (-1, -1)

def simulate(shooters):
    copied = [row[:] for row in board]
    res = 0
    for r in range(N-1, -1, -1):
        dead = set()
        for c in shooters:
            pos = findEnemy(r, c, copied)
            if pos == (-1, -1):
                continue
            dead.add(pos)
        for pr, pc in dead:
            copied[pr][pc] = 0
        res += len(dead)
    return res

answer = 0
for comb in combinations(range(M), 3):
    answer = max(answer, simulate(comb))
print(answer)