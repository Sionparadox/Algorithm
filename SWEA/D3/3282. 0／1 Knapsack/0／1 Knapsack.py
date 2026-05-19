T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    arr = [tuple(map(int, input().split())) for _ in range(N)]
    
    dp = [0]*(K+1)
    for weight, cost in arr:
        for i in range(K, weight-1, -1):
            dp[i] = max(dp[i], dp[i-weight]+cost)
    print(f'#{t} {dp[K]}')
        