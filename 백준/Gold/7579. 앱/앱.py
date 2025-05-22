import sys
input = sys.stdin.readline

N, M = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))

total = sum(cost)
dp = [0]*(total+1)
for i in range(N):
    mem = memory[i]
    co = cost[i]
    for j in range(total, co-1, -1):
        dp[j] = max(dp[j], dp[j-co]+mem)
for i in range(total+1):
    if dp[i]>=M:
        print(i)
        break
