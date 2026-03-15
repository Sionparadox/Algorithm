import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*M for _ in range(N)]
dp[0][0] = board[0][0]

for r in range(N):
    for c in range(M):
        if r>0:
            dp[r][c] = max(dp[r][c], dp[r-1][c]+board[r][c])
        if c>0:
            dp[r][c] = max(dp[r][c], dp[r][c-1]+board[r][c])

print(dp[N-1][M-1])

'''
대각선 이동 x (사탕개수 >=0)
'''