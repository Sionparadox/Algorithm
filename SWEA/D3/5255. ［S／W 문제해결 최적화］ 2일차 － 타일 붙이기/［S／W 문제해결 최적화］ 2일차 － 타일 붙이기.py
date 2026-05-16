T = int(input())
dp = [1,1,3]
for t in range(1, T+1):
    N = int(input())
    L = len(dp)
    if N >= L:
        for i in range(L, N+1):
            dp.append(dp[i-3]+dp[i-2]*2+dp[i-1])
    print(f'#{t} {dp[N]}')