import heapq
INF = float('inf')
TC = int(input())
for tc in range(1, TC+1):
    V, E = map(int, input().split())
    dist = [INF]*(V+1)
    edges = [[] for _ in range(V+1)]
    for _ in range(E):
        A, B, C = map(int, input().split())
        edges[A].append((B, C))
        edges[B].append((A, C))
    
    visited = [False]*(V+1)
    pq = [(0, 1)]
    dist = 0
    cnt = 0
    
    while pq and cnt<V:
        cost, curr = heapq.heappop(pq)
        
        if visited[curr]:
            continue
        visited[curr] = True
        dist += cost
        cnt += 1
        
        for nxt, c in edges[curr]:
            if visited[nxt]:
                continue
            heapq.heappush(pq, (c, nxt))
    
    print(f'#{tc} {dist}')