import sys
input = sys.stdin.readline
INF = float('inf')
n, m, r = map(int, input().split())
items = list(map(int, input().split()))
graph = [[INF]*n for _ in range(n)]
for _ in range(r):
    u, v, w = map(int, input().split())
    graph[u-1][v-1] = w
    graph[v-1][u-1] = w
for i in range(n):
    graph[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
            graph[j][i] = graph[i][j]

answer = 0
for row in graph:
    temp = sum(items[i] for i in range(len(row)) if row[i]<=m)
    answer = max(answer, temp)
print(answer)