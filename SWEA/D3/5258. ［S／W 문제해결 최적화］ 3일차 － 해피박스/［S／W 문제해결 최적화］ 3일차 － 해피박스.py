T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    items = [tuple(map(int, input().split())) for _ in range(M)]
    dp = [0]*(N+1)
    for weight, cost in items:
        for i in range(N, weight-1, -1):
            dp[i] = max(dp[i], dp[i-weight]+cost)
    
    print(f'#{t} {dp[N]}')

'''
dp[w] : w무게만큼 담았을 때 최대 비용
'''