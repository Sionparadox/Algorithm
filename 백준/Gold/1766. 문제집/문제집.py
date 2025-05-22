import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
order = [[x-1 for x in list(map(int, input().split()))] for _ in range(M)]
graph = [[] for _ in range(N)]
indegree = [0]*N

for front, back in order:
    indegree[back] += 1
    graph[front].append(back)
    
answer = []
pq = []
for i in range(N):
    if indegree[i] == 0:
        heapq.heappush(pq, i)

while pq:
    node = heapq.heappop(pq)
    answer.append(node+1)
    for next in graph[node]:
        indegree[next] -= 1
        if indegree[next] == 0:
            heapq.heappush(pq, next)
print(' '.join(map(str,answer)))