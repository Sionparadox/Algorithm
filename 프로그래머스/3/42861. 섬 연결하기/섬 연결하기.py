import heapq
def solution(n, costs):
    answer = 0
    cnt = 0
    graph = [[] for _ in range(n)]
    visited = [False] * n
    
    for u, v, w in costs:
        graph[u].append([v, w])
        graph[v].append([u, w])
    
    pq = []
    heapq.heappush(pq, (0,0))
    while pq and cnt < n:
        d, node = heapq.heappop(pq)
        if visited[node] : continue
        
        visited[node] = True
        answer += d
        cnt += 1
        
        for next, nextD in graph[node]:
            if visited[next] : continue
            heapq.heappush(pq, (nextD, next))
    
    return answer