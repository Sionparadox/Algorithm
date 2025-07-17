import sys
input = sys.stdin.readline

M, N = map(int, input().split())

L = 2*M-1
size = [1]*L

for _ in range(N):
    a,b,c = map(int, input().split())
    for i in range(a, a+b):
        size[i] += 1
    for i in range(a+b, 2*M-1):
        size[i] += 2

board = [[0]*M for _ in range(M)]

for i in range(M):
    board[M - 1 - i][0] = size[i]
for j in range(1, M):
    board[0][j] = size[M - 1 + j]

for i in range(1, M):
    for j in range(1, M):
        board[i][j] = max(board[i-1][j], board[i][j-1], board[i-1][j-1])

for row in board:
    print(*row)