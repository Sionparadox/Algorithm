import sys
from collections import deque
input = sys.stdin.readline

class Dice():
    def __init__(self):
        #TOP, FRONT, LEFT, BACK, RIGHT, BOTTOM
        self.pos = [0,1,2,3,4,5]
    
    def roll(self, dir):
        top, front, left, back, right, bottom = self.pos
        if dir == 0: # U
            self.pos = [front, bottom, left, top, right, back]
        elif dir == 1: # D
            self.pos = [back, top, left, bottom, right, front]
        elif dir == 2: # L
            self.pos = [right, front, top, back, bottom, left]
        elif dir == 3: # R
            self.pos = [left, front, bottom, back, top, right]
    
    def copy(self):
        d = Dice()
        d.pos = self.pos[:]
        return d
        
        
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] #UDLR
def isDice(arr):
    queue = deque()
    visited = set()
    used = [False]*6
    dice = Dice()
    
    for p in range(36):
        r, c = divmod(p, 6)
        if arr[r][c] == 1:
            queue.append((r, c, dice))
            visited.add((r, c))
            used[5] = True
            break
    
    while queue:
        r, c, dice = queue.popleft()
        for d in range(4):
            dr, dc = directions[d]
            nr, nc = r+dr, c+dc
            if nr<0 or nr>5 or nc <0 or nc>5:
                continue
            if (nr, nc) in visited or arr[nr][nc] == 0:
                continue
            
            ndice = dice.copy()
            ndice.roll(d)
            bottom = ndice.pos[5]
            if used[bottom]:
                return False
            queue.append((nr, nc, ndice))
            visited.add((nr, nc))
            used[bottom] = True

    return len(visited) == 6            

for _ in range(3):
    board = [list(map(int, input().split())) for _ in range(6)]
    if isDice(board):
        print('yes')
    else:
        print('no')
