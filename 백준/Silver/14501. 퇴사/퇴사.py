import sys
input = sys.stdin.readline

N = int(input())
T = [0]*N
P = [0]*N

for i in range(N):
    T[i], P[i] = map(int, input().split())

dp = [0]*(N+1)
for i in range(N-1, -1, -1):
    if T[i]+i <= N:
        dp[i] = max(dp[i+1], dp[i+T[i]]+P[i])
    else:
        dp[i] = dp[i+1]
print(dp[0])

'''
dp[i] : i일에 얻을 수 있는 최대수익(역순)

'''    