import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
score = [[0]*M for _ in range(N)]

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] #RDLU

class Dice():
    def __init__(self):
        #TOP, BOTTOM, FRONT, BACK, LEFT, RIGHT
        self.face = [1, 6, 5, 2, 4, 3]
    
    def roll(self, d):
        TOP, BOTTOM, FRONT, BACK, LEFT, RIGHT = self.face
        # east
        if d == 0:
            self.face = [LEFT, RIGHT, FRONT, BACK, BOTTOM, TOP]
        #south
        if d == 1:
            self.face = [BACK, FRONT, TOP, BOTTOM, LEFT, RIGHT]
        #west
        if d == 2:
            self.face = [RIGHT, LEFT, FRONT, BACK, TOP, BOTTOM]
        #north
        if d == 3:
            self.face = [FRONT, BACK, BOTTOM, TOP, LEFT, RIGHT]
    
    def bottom(self):
        return self.face[1]

def BFS(r, c):
    n = board[r][c]
    queue = deque([(r, c)])
    visited = set([(r, c)])
    cnt = 0
    group = [(r, c)]
    while queue:
        cnt += 1
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if nr<0 or nr>=N or nc<0 or nc>=M:
                continue
            if (nr, nc) in visited or board[nr][nc] != n:
                continue
            queue.append((nr, nc))
            visited.add((nr, nc))
            group.append((nr, nc))
    
    for r, c in group:
        score[r][c] = cnt*n

r = c = d = 0
answer = 0
dice = Dice()
for _ in range(K):
    dr, dc = directions[d]
    if not (0<=r+dr<N and 0<=c+dc<M):
        d = (d+2)%4
    dr, dc = directions[d]
    r, c = r+dr, c+dc
    dice.roll(d)
    A = dice.bottom()
    B = board[r][c]
    if score[r][c] == 0:
        BFS(r, c)
    answer += score[r][c]
    if A>B:
        d = (d+1)%4
    elif A<B:
        d = (d-1)%4

print(answer)