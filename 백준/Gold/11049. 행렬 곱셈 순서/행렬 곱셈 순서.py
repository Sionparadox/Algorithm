import sys
input = sys.stdin.readline
N = int(input())
RC = list(map(int, input().split()))

for _ in range(N-1):
    _, c = map(int, input().split())
    RC.append(c)

dp = [[float('inf')]*N for _ in range(N)]
for i in range(N):
    dp[i][i] = 0

for l in range(2, N+1):
    for i in range(N-l+1):
        j = i+l-1
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + RC[i]*RC[k+1]*RC[j+1])

print(dp[0][N-1])