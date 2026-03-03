import sys
input = sys.stdin.readline

M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]
answer = 0

for r in range(M):
    for c in range(N):
        if board[r][c] == 0:
            board[r][c] = 1
            answer = 1
        else:
            board[r][c] = 0

for r in range(1, M):
    for c in range(1, N):
        if board[r][c]:
            board[r][c] = min(board[r-1][c], board[r][c-1], board[r-1][c-1])+1
            answer = max(answer, board[r][c])

print(answer)


'''
0 -> 1, 1,2->0 으로 변경
1 1 1 0 1 1
1 1 1 0 0 1
1 1 0 1 1 1
1 0 1 1 1 1 
0 1 1 1 1 1
1 1 1 1 1 1

(1,1)부터 (N-1,M-1)까지 [r][c]이 0이 아니면 
[r][c] = min([r-1][c], [r][c-1], [r-1][c-1])+1
1 1 1 0 1 1
1 2 2 0 0 1
1 2 0 1 1 1
1 0 1 1 2 2
0 1 1 2 2 3
1 1 2 2 3 3
'''
