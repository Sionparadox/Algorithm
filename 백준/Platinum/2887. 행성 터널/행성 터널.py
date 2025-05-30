import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
planet = []
for i in range(N):
    x, y, z= map(int, input().split())
    planet.append((i, x, y, z))
planetX = sorted(planet, key=lambda x:x[1])
planetY = sorted(planet, key=lambda x:x[2])
planetZ = sorted(planet, key=lambda x:x[3])

graph = defaultdict(list)
for i in range(N-1):
    temp = [(planetX[i], planetX[i+1]), (planetY[i], planetY[i+1]), (planetZ[i], planetZ[i+1])]
    for p in range(3):
        a1, x1, y1, z1 = temp[p][0]
        a2, x2, y2, z2 = temp[p][1]
        cost = min(abs(x1-x2), abs(y1-y2), abs(z1-z2))
        graph[a1].append((cost, a2))
        graph[a2].append((cost, a1))
    
visited = [False]*N
pq = []
heapq.heappush(pq, (0, 0))
answer = 0
while pq:
    cost, now = heapq.heappop(pq)
    if visited[now]:
        continue
    visited[now] = True
    answer += cost
    
    for dist, next in graph[now]:
        if not visited[next]:
            heapq.heappush(pq, (dist, next))

print(answer)
    

'''
X, Y, Z 에 대해 정렬한 3개의 배열을 만들어서 양 옆 인접노드끼리만 그래프에 추가.
임의의 노드 하나 선택해서 해당 노드부터 모든 노드에 대한 거리를 계산.
방문한 노드는 visited처리
'''
