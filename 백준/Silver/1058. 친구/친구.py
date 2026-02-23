import sys
input = sys.stdin.readline
INF = float('inf')

N = int(input())
graph = [input().rstrip() for _ in range(N)]
dist = [[INF]*N for _ in range(N)]

for r in range(N):
    for c in range(N):
        if graph[r][c] == 'Y':
            dist[r][c] = 1

for k in range(N):
    for r in range(N):
        for c in range(N):
            if r == c:
                continue
            dist[r][c] = min(dist[r][c], dist[r][k] + dist[k][c])

answer = 0
for r in range(N):
    answer = max(answer, len(list(filter(lambda x: x<=2, dist[r]))))

print(answer)