TC = int(input())
for _ in range(TC):
    N, M, K = map(int, input().split())
    colors = [c - 1 for c in map(int, input().split())]
    edges = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        edges[u-1].append(v-1)
        edges[v-1].append(u-1)
    
    answer = 0
    dp = [[0]*(1<<K) for _ in range(N)]

    for u in range(N):
        dp[u][1 << colors[u]] = 1

    for mask in range(1, 1 << K):
        cnt = bin(mask).count('1')
        if cnt < 2 or cnt > K:
            continue
        for u in range(N):
            c = colors[u]
            if not (mask & (1 << c)):
                continue
            prev_mask = mask ^ (1 << c)
            for v in edges[u]:
                if prev_mask & (1 << colors[v]):
                    dp[u][mask] += dp[v][prev_mask]
            answer += dp[u][mask]

    print(answer)