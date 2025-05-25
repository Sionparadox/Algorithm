import sys
input = sys.stdin.readline
MOD = 1000000000
N = int(input())
dp = [[[0]*1024 for _ in range(10)] for _ in range(N+1)]

for i in range(1,10):
    dp[1][i][1<<i] = 1

for pos in range(2,N+1):
    for num in range(10):
        for mask in range(1024):
            if num > 0:
                dp[pos][num][mask | (1<<num)] += dp[pos-1][num-1][mask]
                dp[pos][num][mask | (1<<num)] %= MOD
            if num < 9:
                dp[pos][num][mask | (1<<num)] += dp[pos-1][num+1][mask]
                dp[pos][num][mask | (1<<num)] %= MOD

answer = 0
for i in range(10):
    answer += dp[N][i][1023]
    answer %= MOD
print(answer)