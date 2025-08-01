import sys
input = sys.stdin.readline

N, T = map(int, input().split())
dp = [0]*(T+1)

for _ in range(N):
    time, score = map(int, input().split())
    for i in range(T, time-1, -1):
        dp[i] = max(dp[i], dp[i-time]+score)

print(dp[T])

'''
냅색 문제
dp[i] : i시간으로 받을 수 있는 최대 점수
'''