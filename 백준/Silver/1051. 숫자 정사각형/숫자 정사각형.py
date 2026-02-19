import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().strip())))

L = 1
for r in range(N):
    for c in range(M):
        for l in range(min(N-r-1, M-c-1), L-1, -1):
            if board[r][c] == board[r+l][c] == board[r][c+l] == board[r+l][c+l]:
                L = l+1
                break

print(L**2)