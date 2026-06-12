TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    tasks = [tuple(map(int, input().split())) for _ in range(N)]
    dp = [0]*(M+1)
    tasks.sort(key=lambda x:x[1])
    idx = 0
    for t in range(1, M+1):
        dp[t] = dp[t-1]
        while idx < N and tasks[idx][1] == t:
            s, e, c = tasks[idx]
            dp[t] = max(dp[t], dp[s-1]+c)
            idx += 1
    
    print(f'#{tc} {dp[M]}')