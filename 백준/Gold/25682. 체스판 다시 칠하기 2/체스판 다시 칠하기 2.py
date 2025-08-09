import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
board = [input().strip() for _ in range(N)]

white_cell = [[0]*(M+1) for _ in range(N+1)]
black_cell = [[0]*(M+1) for _ in range(N+1)]

for r in range(N):
    for c in range(M):
        if (r+c) % 2 == 0:
            if board[r][c] == 'B':
                white_cell[r+1][c+1] = 1
            else:
                black_cell[r+1][c+1] = 1
        else:
            if board[r][c] == 'B':
                black_cell[r+1][c+1] = 1
            else:
                white_cell[r+1][c+1] = 1

for r in range(1, N+1):
    for c in range(1, M+1):
        white_cell[r][c] += white_cell[r-1][c] + white_cell[r][c-1] - white_cell[r-1][c-1]
        black_cell[r][c] += black_cell[r-1][c] + black_cell[r][c-1] - black_cell[r-1][c-1]

answer = float('inf')
for i in range(1, N-K+2):
    for j in range(1, M-K+2):
        x, y = i+K-1, j+K-1
        w = white_cell[x][y] - white_cell[i-1][y] - white_cell[x][j-1] + white_cell[i-1][j-1]
        b = black_cell[x][y] - black_cell[i-1][y] - black_cell[x][j-1] + black_cell[i-1][j-1]
        answer = min(answer, w, b)
print(answer)