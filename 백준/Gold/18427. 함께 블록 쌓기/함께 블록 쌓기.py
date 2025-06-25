import sys
input = sys.stdin.readline

N, M, H = map(int, input().split())
blocks = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*(H+1) for _ in range(N+1)]
dp[0][0] = 1

for i in range(1, N+1):
    for j in range(H+1):
        dp[i][j] += dp[i-1][j]
        
        for k in blocks[i-1]:
            if j >= k:
                dp[i][j] += dp[i-1][j-k]

print(dp[N][H]%10007)

'''
dp[i][h] : i번째 사람까지의 블록을 사용해서 만들 수 있는 블록의 높이가 h인 경우의 수
i번째 사람이 블록을 안쓸 경우 dp[i][h] += dp[i-1][h]
i번째 사람이 블록을 쓸 경우 가진 블록에 대해 dp[i][h] += dp[i-1][h-k]
'''