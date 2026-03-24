import sys
input = sys.stdin.readline
INF = float('inf')

N, M = map(int, input().split())
dist = [[INF]*(N+1) for _ in range(N+1)]
answer = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    u, v, t = map(int, input().split())
    dist[u][v] = t
    dist[v][u] = t
    answer[v][u] = u
    answer[u][v] = v

for i in range(1, N+1):
    dist[i][i] = 0

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            nd = dist[i][k] + dist[k][j]
            if dist[i][j] > nd:
                dist[i][j] = nd
                answer[i][j] = answer[i][k]

for row in answer[1:]:
    print(*[x if x != 0 else '-' for x in row[1:]])