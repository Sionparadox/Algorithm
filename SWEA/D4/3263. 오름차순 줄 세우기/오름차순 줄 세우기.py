TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = list(map(int, input().split()))
    dp = [0]*(N+1)
    for n in arr:
        dp[n] = dp[n-1]+1
    print(f'#{tc} {N-max(dp)}')