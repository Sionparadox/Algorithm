import sys
input = sys.stdin.readline

N = int(input())
value = list(map(int, input().split()))
dp = [0]*(N+1)

for i in range(1, N+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], dp[i-j] + value[j-1])

print(dp[N])


'''
dp[i] : i장을 얻기위한 최대값
dp[i] = dp[i-k]+Pk (1<=k<=i)
'''