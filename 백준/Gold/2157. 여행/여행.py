import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(K):
    s, e, w = map(int, input().split())
    if s<e:
        graph[s].append((e, w))

dp = [[-1]*(N+1) for _ in range(M+1)]
dp[1][1] = 0
for s in range(1, N+1):
    for i in range(1, M):
        if dp[i][s] == -1:
            continue
        for e, v in graph[s]:
            dp[i+1][e] = max(dp[i+1][e], dp[i][s]+v)

print(max(dp[i][N] for i in range(1, M+1)))
        

'''
dp[i][j] : i개의 도시를 지나 j번쨰 도시에 도착
'''