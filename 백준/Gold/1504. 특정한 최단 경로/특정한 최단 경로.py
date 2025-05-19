import sys
import heapq
input = sys.stdin.readline

N, E = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(E)]
needs = [x-1 for x in list(map(int, input().split()))]

graph = [[] for _ in range(N)]
for u, v, w in edges:
    graph[u-1].append((v-1,w))
    graph[v-1].append((u-1,w))

def dijkstra(start):
    dist = [float('inf')]*N
    dist[start] = 0
    pq = []
    heapq.heappush(pq, (0, start))
    while pq:
        distance, node = heapq.heappop(pq)
        
        if dist[node] < distance:
            continue
        for next, d in graph[node]:
            newDistance = distance + d
            if newDistance < dist[next]:
                dist[next] = newDistance
                heapq.heappush(pq, (newDistance, next))
    return dist   
    
startDist = dijkstra(0)
endDist = dijkstra(N-1)
visitDist = dijkstra(needs[0])
answer = visitDist[needs[1]]
answer += min(startDist[needs[0]] + endDist[needs[1]], startDist[needs[1]] + endDist[needs[0]])
print(answer if answer != float('inf') else -1)