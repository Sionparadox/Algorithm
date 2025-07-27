import sys
import copy
input = sys.stdin.readline

M, S = map(int, input().split())
board = [[[] for _ in range(4)] for _ in range(4)]
for _ in range(M):
    x, y, d = map(int, input().split())
    board[x-1][y-1].append(d-1)
shark = tuple(x-1 for x in map(int, input().split()))

directions = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)] #시계
dir4 = [(-1, 0), (0, -1), (1, 0), (0, 1)] #사전순
smells = [[0]*4 for _ in range(4)]

def move():
    res = [[[] for _ in range(4)] for _ in range(4)]
    for r in range(4):
        for c in range(4):
            for d in board[r][c]:
                isMoved = False
                for k in range(8):
                    nd = (d-k)%8
                    dr, dc = directions[nd]
                    nr, nc = r+dr, c+dc
                    if nr<0 or nr>=4 or nc<0 or nc>=4:
                        continue
                    if (nr, nc) == shark or smells[nr][nc] >0:
                        continue
                    isMoved=True
                    res[nr][nc].append(nd)
                    break
                if not isMoved:
                    res[r][c].append(d)
    
    return res
                
def sharkMove(r, c, k, val, path, arr):
    if k==3:
        return val, path, arr
    
    res = (-1, '', [])
    for d in range(4):
        dr, dc = dir4[d]
        nr, nc = r+dr, c+dc
        if 0<=nr<4 and 0<=nc<4:
            fishes = board[nr][nc]
            board[nr][nc] = []
            v, p, ar = sharkMove(nr, nc, k+1, val+len(fishes), path+str(d), arr+[(nr, nc)])
            if v>res[0] or (v==res[0] and p<res[1]):
                res = (v, p, ar)
            board[nr][nc] = fishes
    
    return res

for _ in range(S):
    copied = copy.deepcopy(board)
    board = move()
    _, _, dead = sharkMove(shark[0], shark[1], 0, 0, '', [])
    for r, c in dead:
        if board[r][c]:
            smells[r][c] = 3
        board[r][c] = []
    shark = tuple(dead[-1])
    for r in range(4):
        for c in range(4):
            smells[r][c] = max(smells[r][c]-1, 0)
            board[r][c].extend(copied[r][c])

answer = 0
for r in range(4):
    for c in range(4):
        answer += len(board[r][c])

print(answer)