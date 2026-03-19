import sys, heapq
input = sys.stdin.readline
INF = float('inf')

N, M, K = map(int, input().split())
roads = [[] for _ in range(N)]
for _ in range(M):
    u, v, t = map(int, input().split())
    roads[u-1].append((v-1, t))
    roads[v-1].append((u-1, t))

pq = []
dist = [[INF]*(K+1) for _ in range(N)]
dist[0][0] = 0
heapq.heappush(pq, (0, 0, 0))

while pq:
    time, curr, k = heapq.heappop(pq)
    if dist[curr][k] < time:
        continue
    
    for nxt, nt in roads[curr]:
        if dist[nxt][k] > dist[curr][k]+nt:
            dist[nxt][k] = dist[curr][k]+nt
            heapq.heappush(pq, (dist[curr][k]+nt, nxt, k))
        
        if k<K and dist[nxt][k+1] > dist[curr][k]:
            dist[nxt][k+1] = dist[curr][k]
            heapq.heappush(pq, (dist[curr][k], nxt, k+1))

print(min(dist[N-1]))


'''
다익스트라 -> dist[i][k] : k번 포장해서 i까지 가는 최소거리
dist[nxt][k] = dist[curr][k]+d
dist[nxt][k+1] = dist[curr][k]

pq 우선순위 : (거리, 노드, 포장횟수)

'''