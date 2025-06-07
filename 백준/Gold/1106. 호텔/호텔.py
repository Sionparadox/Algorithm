import sys
input = sys.stdin.readline

C, N = map(int, input().split())
cities = [tuple(map(int, input().split())) for _ in range(N)]

dp = [float('inf')]*(C+101)
dp[0] = 0

for cost, value in cities:
    for i in range(value, C+101):
        dp[i] = min(dp[i], dp[i-value]+cost)

print(min(dp[C:]))

'''
dp[i] : i 고객 수를 얻기 위한 최소 비용
N개의 도시에 대해 value부터 C+101까지 돌림
dp[i] = min(dp[i], dp[i-value]+cost)
'''