import heapq
INF = float('inf')

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    M = int(input())
    edges = [[] for _ in range(N+1)]
    for _ in range(M):
        s, e, c = map(int, input().split())
        edges[s].append((e, c))
        edges[e].append((s, c))
    
    visited = [False]*(N+1)
    pq = [(0, 1)]
    answer = 0
    cnt = 0
    while pq and cnt < N:
        cost, curr = heapq.heappop(pq)
        
        if visited[curr]:
            continue
        
        visited[curr] = True
        answer += cost
        cnt += 1
        
        for nxt, c in edges[curr]:
            if not visited[nxt]:
                heapq.heappush(pq, (c, nxt))
    
    print(f'#{tc} {answer}')