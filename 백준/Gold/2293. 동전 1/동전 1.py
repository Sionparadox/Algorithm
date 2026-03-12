import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
dp = [0]*(K+1)
dp[0] = 1

for coin in coins:
    for i in range(coin, K+1):
        dp[i] += dp[i-coin]
        
print(dp[K])

'''
dp[i] : i원을 만들 수 있는 경우의 수
dp[i] : sum(dp[i-coin])

i에 대해 돌리니 중복 문제 발생
coin에 대해 반복
'''