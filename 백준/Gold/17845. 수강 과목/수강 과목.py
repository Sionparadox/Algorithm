import sys
input = sys.stdin.readline

N, K = map(int, input().split())

importance = [0]*(K+1)
time = [0]*(K+1)
for k in range(1,K+1):
    i, t = map(int, input().split())
    importance[k] = i
    time[k] = t

dp = [0]*(N+1)
for k in range(1,K+1):
    imp = importance[k]
    tm = time[k]
    for i in range(N, tm-1, -1):
        dp[i] = max(dp[i], dp[i-tm]+imp)

print(dp[N])

'''
dp[i] : i 공부시간으로 얻을 수 있는 최대 중요도
'''