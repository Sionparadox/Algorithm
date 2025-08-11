import sys
input = sys.stdin.readline
MOD = 1_000_000_003

N = int(input())
K = int(input())
dp = [[0]*(K+1) for _ in range(N+1)]
for i in range(1, N+1):
    dp[i][0] = 1
    dp[i][1] = i

for n in range(2, N+1):
    for k in range(2, K+1):
        if n == N:
            dp[n][k] = (dp[n-3][k-1] + dp[n-1][k]) % MOD
        else:
            dp[n][k] = (dp[n-2][k-1] +  dp[n-1][k]) % MOD
print(dp[N][K])

'''
원말고 직선으로 변형 (1,N은 같이 색칠 X)
dp[n][k] : n개 색을 k개 칠하는 경우의 수

1번을 칠할 때 : N-3개의 색을 K-1개 칠하는 경우의 수(dp[N-3][K-1])
1 2 3 4 5 6 7 8
o x - - - - - x
1번을 안칠할때 : N-1개의 색을 K개 칠하는 경우의 수(dp[N-1][k])
1 2 3 4 5 6 7 8
x - - - - - - -
dp[N][K] = dp[N-1][K] + dp[N-3][K-1]

n이 N이 아닐 떄
n을 칠할떄 : dp[n-2][k-1]
1 2 3 4 5 6 7/8
- - - - - x o
n을 안칠할 때 : dp[n-1][k]
1 2 3 4 5 6 7/8
- - - - - - x
'''