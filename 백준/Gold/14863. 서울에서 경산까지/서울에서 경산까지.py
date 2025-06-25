import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1]*(K+1) for _ in range(N+1)]
dp[0][0] = 0

for i in range(1, N+1):
    w1, v1, w2, v2 = arr[i-1]
    for j in range(K+1):
        if dp[i-1][j] == -1:
            continue
        
        if j+w1 <= K:
            dp[i][j+w1] = max(dp[i][j+w1], dp[i-1][j]+v1)
        
        if j+w2 <= K:
            dp[i][j+w2] = max(dp[i][j+w2], dp[i-1][j]+v2)

print(max(dp[N]))

'''
dp[i][j] : i번째 도시까지 j분동안 이동해서 얻은 최대 수익
dp[i][j+time1] = dp[i-1][j]+value1
'''