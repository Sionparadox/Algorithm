import sys
import heapq
input = sys.stdin.readline
INF = float('inf')

N = int(input())
M = int(input())
graph = [[] for _ in range(N)]
for _ in range(M):
    s, e, w = map(int, input().split())
    graph[s-1].append((e-1,w))
S, E = map(int, input().split())
S -= 1
E -= 1



dist = [INF] * N
route = [[] for _ in range(N)]
pq = []
dist[S] = 0
prev = [-1] * N
heapq.heappush(pq, (0,S))
while pq:
    distance, node = heapq.heappop(pq)
    
    if distance > dist[node]: continue
    for next, d in graph[node]:
        nd = d+distance
        if nd <dist[next]:
            dist[next] = nd
            prev[next] = node
            heapq.heappush(pq, (nd, next))

path = []
node = E
while node != -1:
    path.append(node+1)
    node = prev[node]
path.reverse()
print(dist[E])
print(len(path))
print(' '.join(map(str, path)))