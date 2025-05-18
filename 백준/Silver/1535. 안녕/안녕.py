import sys
input = sys.stdin.readline

HEALTH = 100

N = int(input())

costs = list(map(int, input().split()))
gets = list(map(int, input().split()))
dp = [0] * (HEALTH)

for cost, joy in zip(costs, gets):
    for h in range(HEALTH-1, cost-1, -1):
        dp[h] = max(dp[h], dp[h-cost]+joy)
print(dp[HEALTH-1])