import sys, heapq
input = sys.stdin.readline
INF = float('inf')

def dijkstra(start):
    dist = [INF]*(N+1)
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, curr = heapq.heappop(pq)
        if dist[curr] < d:
            continue
        
        for nxt, nd in graph[curr]:
            new_d = d+nd
            if dist[nxt] > new_d:
                dist[nxt] = new_d
                heapq.heappush(pq, (new_d, nxt))
    
    return dist


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        u, v, d = map(int, input().split())
        graph[u].append((v, d))
        graph[v].append((u, d))
    
    K = int(input())
    friends = list(map(int, input().split()))
    dist_sum = [0]*(N+1)
    for pos in friends:
        dist = dijkstra(pos)
        for i in range(1, N+1):
            dist_sum[i] += dist[i]
    
    min_value = INF
    min_idx = -1
    for i in range(1, N+1):
        if dist_sum[i] < min_value:
            min_idx = i
            min_value = dist_sum[i]
    
    print(min_idx)
    
