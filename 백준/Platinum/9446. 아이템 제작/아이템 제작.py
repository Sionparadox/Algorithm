import sys
from collections import defaultdict
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
cost = [0]+list(map(int, input().split()))
graph = defaultdict(list)

for _ in range(M):
    a, x, y = map(int, input().split())

    graph[x].append((a, y))
    graph[y].append((a, x))

dp = cost[:]
pq = []
for i in range(1, N+1):
    heapq.heappush(pq, (dp[i], i))

while pq:
    cost, item = heapq.heappop(pq)
    if dp[item] < cost:
        continue
    
    for nxt, ingredient in graph[item]:
        new_cost = dp[item]+dp[ingredient]
        if new_cost < dp[nxt]:
            dp[nxt] = new_cost
            heapq.heappush(pq, (dp[nxt], nxt))

print(dp[1])