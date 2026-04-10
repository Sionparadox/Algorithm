import sys
input = sys.stdin.readline
MOD = 10007

N = int(input())
dp = [1, 1]
for x in range(2, N+1):
    dp.append((dp[-1]+dp[-2]) % MOD)

print(dp[N])