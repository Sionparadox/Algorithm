import sys
from collections import deque
input = sys.stdin.readline

R, C, N = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]

def explode():
    res = [['O']*C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if board[r][c] == 'O':
                res[r][c] = '.'
                for dr ,dc in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                    nr, nc = r+dr, c+dc
                    if 0<=nr<R and 0<=nc<C and res[nr][nc] == 'O':
                        res[nr][nc] = '.'
    return res

if N == 1:
    print('\n'.join(''.join(row) for row in board))

elif N % 2 == 0:
    print('\n'.join('O'*C for _ in range(R)))

else:
    board = explode()
    if N % 4 == 3:
        print('\n'.join(''.join(row) for row in board))
    else:
        board = explode()
        print('\n'.join(''.join(row) for row in board))

'''
N % 4 == 1 : 기본
N % 2 == 0 : 전체
N % 4 == 3 : 반대
첫 폭발 이후로 사이클이 생김
'''