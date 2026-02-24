import sys
input = sys.stdin.readline
MOD = 10007

N = int(input())
dp = [[0]*10 for _ in range(N+1)]
dp[1] = [1]*10

for n in range(2, N+1):
    dp[n][0] = 1
    for k in range(1, 10):
        dp[n][k] = (dp[n-1][k] + dp[n][k-1]) % MOD

print(sum(dp[N]) % MOD)

'''
끝자리 수에 따라 다음 올 수 있는 수가 달라짐.
dp[n][k] : n자리 수 중 끝이 k인 수의 오르막 수 개수
dp[n+1][0] = dp[n][0]
dp[n+1][1] = dp[n][1] + dp[n][0]
dp[n+1][2] = dp[n][2] + dp[n][1] + dp[n][0]
dp[n+1][3] = dp[n][3] + dp[n][2] + dp[n][1] + dp[n][0] = dp[n][3] + dp[n+1][2]

dp[n][k] = dp[n-1][k] + dp[n][k-1]
'''