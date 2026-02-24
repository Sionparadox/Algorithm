import sys
input = sys.stdin.readline
INF = float('inf')

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

dp = [INF]*(K+1)
dp[0] = 0

for i in range(1, K+1):
    for coin in coins:
        if i >= coin:
            dp[i] = min(dp[i], dp[i-coin]+1)

print(dp[K] if dp[K] != INF else -1)

'''
dp[i] : i원을 만드는 최소 동전 개수
동전 배열에 대해서 dp[i] = min(dp[i-coin] + 1)[반복]
'''