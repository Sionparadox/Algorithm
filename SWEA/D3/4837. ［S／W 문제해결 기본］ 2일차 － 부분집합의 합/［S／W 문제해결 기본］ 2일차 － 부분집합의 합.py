T = int(input())
dp = [[0]*79 for _ in range(13)]
dp[0][0] = 1
for k in range(1, 13):
    for i in range(12, 0, -1):
        for j in range(78, k-1, -1):
            dp[i][j] += dp[i-1][j-k]

for t in range(1, T+1):
    N, K = map(int, input().split())
    left = N*(N+1)//2
    right = 13*N-left
    if K<left or K>right:
        print(f'#{t} 0')
        continue
    print(f'#{t} {dp[N][K]}')