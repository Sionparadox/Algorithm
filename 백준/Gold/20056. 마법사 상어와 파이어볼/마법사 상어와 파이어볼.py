import sys
input = sys.stdin.readline

directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1,-1), (0, -1), (-1, -1)]

N, M, K = map(int, input().split())
fireballs = []
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fireballs.append([r-1, c-1, m, s, d])


def move():
    board = {} #cnt, m, s, d
    
    for r, c, m, s, d in fireballs:
        dr, dc = directions[d]
        nr, nc = (r+dr*s)%N, (c+dc*s)%N
        if (nr, nc) in board:
            board[(nr, nc)][0] += 1
            board[(nr, nc)][1] += m
            board[(nr, nc)][2] += s
            if board[(nr, nc)][3] != -1 and board[(nr, nc)][3] % 2 != d%2:
                board[(nr, nc)][3] = -1
        else:
            board[(nr, nc)] = [1, m, s, d]
    res = []
    for r, c in board:
        cnt, m, s, d = board[(r, c)]
        if cnt == 1:
            res.append((r, c, m, s, d))
        else:
            m //= 5
            s //= cnt
            if m == 0:
                continue
            for nd in range(d==-1, 8, 2):
                res.append((r, c, m, s, nd))
    
    return res
 
for _ in range(K):
    fireballs = move()

answer = 0
for _,_,m,_,_ in fireballs:
    answer += m
print(answer)