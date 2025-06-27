import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

N, M = map(int, input().split())
graph = defaultdict(list)

for t in range(M):
    u, v = map(int, input().split())
    graph[u-1].append((v-1, t))
    graph[v-1].append((u-1, t))

dp = [float('inf')]*N
dp[0] = 0

pq = []
heapq.heappush(pq, (0, 0))
while pq:
    t, node = heapq.heappop(pq)
    if dp[node] < t:
        continue
    
    for nxt, time in graph[node]:
        if time < t:
            time += ((t-time+M-1) // M) * M
        if dp[nxt] > time+1:
            dp[nxt] = time+1
            heapq.heappush(pq, (time+1, nxt))

print(dp[N-1])
