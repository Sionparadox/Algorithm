import sys, heapq
input = sys.stdin.readline
INF = float('inf')

N, M, K = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, t = map(int, input().split())
    graph[u].append((v, t))

dist = [[] for _ in range(N+1)]
dist[1].append(0)
pq = [(0, 1)]

while pq:
    time, curr = heapq.heappop(pq)
    
    for nxt, t in graph[curr]:
        new_time = time + t
        
        if len(dist[nxt]) < K:
            heapq.heappush(dist[nxt], -new_time)
            heapq.heappush(pq, (new_time, nxt))
        
        elif -dist[nxt][0] > new_time:
            heapq.heappop(dist[nxt])
            heapq.heappush(dist[nxt], -new_time)
            heapq.heappush(pq, (new_time, nxt))

for i in range(1, N+1):
    if len(dist[i]) < K:
        print(-1)
    else:
        print(-dist[i][0])


'''
기본적으로 다익스트라 사용
dist[i][k] : i로 가는 k번째 최단경로
dist[i] = []로 선언한 후 i에 도착할 때마다 넣기(dist[i]자체를 최대힙으로 관리?)
dist[i]가 K개가 채워지기 전에는 무조건 push
이후는 dist[i]의 최댓값보다 본인 값이 작으면 push

'''