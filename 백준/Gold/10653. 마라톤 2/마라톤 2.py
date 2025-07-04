import sys
input = sys.stdin.readline

N, K  = map(int, input().split())
checkpoints = [tuple(map(int, input().split())) for _ in range(N)]

dp = [[float('inf')]*(K+1) for _ in range(N)]
dp[0][0] = 0

for k in range(K+1):
    for i in range(1, N):
        for j in range(i):
            skip = i-j-1
            if k>= skip:
                dist = dp[j][k-skip] + abs(checkpoints[i][0]-checkpoints[j][0]) +  abs(checkpoints[i][1]-checkpoints[j][1])
                dp[i][k] = min(dp[i][k], dist)
            

print(min(dp[N-1]))

'''
dp[i][k] : k개 뛰어넘어서 i번 체크포인트에 도착하는 최소거리
i,j(i<j)의 모든 쌍에 대해 j의 모든 통과 경우(k)에 대해 dp[i][k]를 변경
'''