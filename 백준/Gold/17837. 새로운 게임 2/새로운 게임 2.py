import sys
input = sys.stdin.readline

N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
pos = {}
token_dir = [None]*K
token = [[[] for _ in range(N)] for _ in range(N)]
directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
for i in range(K):
    r, c, d = map(int, input().split())
    pos[i] = (r-1, c-1)
    token[r-1][c-1].append(i)
    token_dir[i] = d-1

def reverseDirection(d):
    if d<2:
        return 1-d
    else:
        return 5-d

def move(idx, isReverse = False):
    r, c = pos[idx]
    d = token_dir[idx]
    dr, dc = directions[d]
    nr, nc = r+dr, c+dc
    index = token[r][c].index(idx)
    stack = token[r][c][index:]
    token[r][c] = token[r][c][:index]
    
    if nr < 0 or nr >= N or nc <0 or nc >= N or board[nr][nc] == 2:
        token_dir[idx] = reverseDirection(d)
        dr, dc = directions[token_dir[idx]]
        nr, nc = r+dr, c+dc
        if nr < 0 or nr >= N or nc <0 or nc >= N or board[nr][nc] == 2:
            token[r][c].extend(stack)
            return False
    if board[nr][nc] == 1:
        stack.reverse()
    
    for tkn in stack:
        pos[tkn] = (nr, nc)
        token[nr][nc].append(tkn)
        
    return len(token[nr][nc]) >=4
        
    
for t in range(1, 1001):
    for k in range(K):
        isFinish = move(k)
        
        if isFinish:
            print(t)
            exit(0)
print(-1)
