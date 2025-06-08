import sys
input = sys.stdin.readline

N = int(input())
time = [0]*N
profit = [0]*N

for i in range(N):
    time[i], profit[i] = map(int, input().split())

dp = [0]*(N+1)

for i in range(N-1, -1, -1):
    if i+time[i] < N+1:
        dp[i] = max(dp[i+1], dp[i+time[i]]+profit[i])
    else :
        dp[i] = dp[i+1]

print(dp[0])