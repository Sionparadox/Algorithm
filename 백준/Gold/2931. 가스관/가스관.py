import sys
input = sys.stdin.readline

R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] #URDL
pipes = ['|', '-', '+', '1', '2', '3', '4']
pos = (-1, -1)
d = -1
for i in range(R):
    for j in range(C):
        if board[i][j] == 'M':
            pos = (i, j)
            for didx in range(4):
                ni, nj = i+directions[didx][0], j+directions[didx][1]
                if 0<=ni<R and 0<=nj<C and board[ni][nj] in pipes:
                    d = didx
                    break
            break
    if pos != (-1, -1):
        break

def pipe(p, d):
    if p == '1':
        if d == 0:
            return 1
        if d == 3:
            return 2
    elif p == '2':
        if d == 2:
            return 1
        if d == 3:
            return 0
    elif p == '3':
        if d == 1:
            return 0
        if d == 2:
            return 3
    elif p == '4':
        if d == 0:
            return 3
        if d == 1:
            return 2
    elif p == '|':
        if d in (0, 2):
            return d
    elif p == '-':
        if d in (1, 3):
            return d
    else:
        return d
    
    return -1

def check(r, c, d):
    while True:
        dr, dc = directions[d]
        r, c = r+dr, c+dc
        if r<0 or r>=R or c<0 or c>=C:
            return False
        if board[r][c] == 'Z':
            return True
        d = pipe(board[r][c], d)
        if d == -1:
            return False
        

blank = (-1, -1)
while True:
    r, c = pos
    dr, dc = directions[d]
    r, c = r+dr, c+dc
    if board[r][c] == '.':
        blank = (r, c)
        break
    d = pipe(board[r][c], d)
    pos = (r, c)

for p in pipes:
    board[blank[0]][blank[1]] = p
    if check(pos[0], pos[1], d):
        print(blank[0]+1, blank[1]+1, p)
        break

'''
M부터 파이프를 따라 이동하며 빈곳이 나오면 멈추고 현재 위치와 방향을 기억해둠.
이후 빈칸에 하나씩 채워보며 이동이 가능한 모양만 찾아냄
'''