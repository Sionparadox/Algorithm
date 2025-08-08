import sys
input = sys.stdin.readline
INF = float('inf')

V, E = map(int, input().split())
graph = [[INF]*V for _ in range(V)]
for _ in range(E):
    s, e, d = map(int, input().split())
    graph[s-1][e-1] = d

for k in range(V):
    for i in range(V):
        if graph[i][k] == INF:
            continue
        for j in range(V):
            if graph[k][j] == INF:
                continue
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

answer = INF
for i in range(V):
    answer = min(answer, graph[i][i])

print(answer if answer != INF else -1)