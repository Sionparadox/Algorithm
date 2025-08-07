import sys
input = sys.stdin.readline
INF = float('inf')

def solve():
    dp = [[INF]*(M+1) for _ in range(N)]
    dp[0][0] = 0
    
    for j in range(M+1):
        for i in range(N):
            if dp[i][j] != INF:
                for nxt, cost, time in graph[i]:
                    if j+cost <= M:
                        dp[nxt][j+cost] = min(dp[nxt][j+cost], dp[i][j]+time)
    
    return min(dp[N-1])
    

T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(K):
        u, v, c, t = map(int, input().split())
        u, v = u-1, v-1
        graph[u].append((v, c ,t))

    answer = solve()
    print(answer if answer != INF else 'Poor KCM')


'''
다익스트라 -> 시간초과
냅색?

'''