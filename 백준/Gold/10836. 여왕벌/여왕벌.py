import sys
input = sys.stdin.readline

M, N = map(int, input().split())
board = [[1]*M for _ in range(M)]

def side(arr):
    idx = 0
    for r in range(M-1, -1, -1):
        while arr[idx] == 0:
            idx += 1
        board[r][0] += idx
        arr[idx] -= 1
    for c in range(1, M):
        while arr[idx] == 0:
            idx += 1
        board[0][c] += idx
        arr[idx] -= 1
    
def grow():
    for i in range(1, M):
        for j in range(1, M):
            board[i][j] = max(board[i-1][j], board[i][j-1], board[i-1][j-1])

for _ in range(N):
    arr = list(map(int, input().split()))
    side(arr)
grow()

print('\n'.join(' '.join(map(str,row)) for row in board))
