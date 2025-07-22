import sys
input = sys.stdin.readline

N = int(input())
board = [[0]*101 for _ in range(101)]
directions = [(0, 1), (-1, 0), (0, -1), (1, 0)] #RULD

def curve(r, c, dirs, k):
    if k >= g:
        return
    
    res = dirs[:]
    for d in dirs[::-1]:
        nd = (d+1)%4
        dr, dc = directions[nd]
        res.append(nd)
        r, c = r+dr, c+dc
        board[r][c] = 1
    
    curve(r, c, res, k+1)

def square():
    res = 0
    for r in range(100):
        for c in range(100):
            if board[r][c] and board[r+1][c] and board[r][c+1] and board[r+1][c+1]:
                res += 1
    return res

for _ in range(N):
    c, r, d, g = map(int, input().split())
    board[r][c] = 1
    dr, dc = directions[d]
    board[r+dr][c+dc] = 1
    curve(r+dr, c+dc, [d], 0)

print(square())

'''
보드에 점에 대해 방문체크를 하고
함수에 재귀로 방향 배열을 넣어 돌리기
'''