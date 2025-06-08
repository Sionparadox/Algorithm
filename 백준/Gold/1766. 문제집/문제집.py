import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())

indegree = [0]*(N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    indegree[e] += 1
    
pq = []
for i in range(1, N+1):
    if indegree[i] == 0:
        heapq.heappush(pq, i)

answer = []
while pq:
    now = heapq.heappop(pq)
    answer.append(now)
    
    for next in graph[now]:
        indegree[next] -= 1
        if indegree[next] == 0:
            heapq.heappush(pq, next)
    
print(' '.join(map(str, answer)))