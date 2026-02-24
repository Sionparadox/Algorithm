import sys
input = sys.stdin.readline
MOD = 1000000000

N, K = map(int, input().split())
dp = [[0]*(N+1) for _ in range(K+1)]

for i in range(K+1):
    dp[i][0] = 1
for i in range(N+1):
    dp[1][i] = 1

for i in range(2, K+1):
    for j in range(1, N+1):
        dp[i][j] = (dp[i-1][j] + dp[i][j-1])%MOD

print(dp[K][N])

'''
dp[i][j] : i개의 수로 합 j를 만들 경우의 수

1 j : 1
i 0 : 1

2 1 : 2
2 2 : 3
2 3 : 4
3 1 : 3
3 2 : 6
3 3 : 10

dp[i][j] = dp[i-1][j] + dp[i][j-1]
'''
