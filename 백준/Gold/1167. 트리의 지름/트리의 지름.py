import sys
import heapq
input = sys.stdin.readline
INF = float('inf')

V = int(input())
graph = [[] for _ in range(V+1)]
#initialize graph
for _ in range(V):
    arr = list(map(int, input().split()))
    n = arr[0]
    for i in range(1, len(arr)-1, 2):
        graph[n].append((arr[i],arr[i+1]))

#dijkstra
def dijkstra(start):
    dist = [INF]*(V+1)
    dist[start] = 0
    pq = []
    heapq.heappush(pq, (0, start))
    
    while pq:
        distance, node = heapq.heappop(pq)
        
        if dist[node] < distance : continue
        
        for next, d in graph[node]:
            newDistance = distance + d
            if newDistance < dist[next]:
                dist[next] = newDistance
                heapq.heappush(pq, (newDistance, next))
    return dist


d = dijkstra(1)
endNode = -1
maxVal = 0
for i in range(1,V+1):
    if d[i] > maxVal:
        endNode = i
        maxVal = d[i]

length = dijkstra(endNode)
print(max(length[1:]))