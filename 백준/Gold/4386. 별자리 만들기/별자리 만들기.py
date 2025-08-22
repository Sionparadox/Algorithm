import sys
import heapq
input = sys.stdin.readline

N = int(input())
stars = [tuple(map(float, input().split())) for _ in range(N)]

distance = [[0.0]*N for _ in range(N)]
def calc(a, b):
    x1, y1 = stars[a]
    x2, y2 = stars[b]
    return ((x2-x1)**2 + (y2-y1)**2)**(0.5)

for i in range(N-1):
    for j in range(i+1, N):
        distance[i][j] = distance[j][i] = calc(i, j)

visited = [False]*N
pq = []
heapq.heappush(pq, (distance[0][0], 0))
answer = 0
while pq:
    d, node = heapq.heappop(pq)
    if visited[node] : continue
    visited[node] = True
    answer += d
    for nxt in range(N):
        if visited[nxt]: continue
        heapq.heappush(pq, (distance[node][nxt], nxt))

print(answer)