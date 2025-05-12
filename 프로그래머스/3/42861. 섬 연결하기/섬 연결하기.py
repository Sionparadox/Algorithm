from queue import PriorityQueue
def solution(n, costs):
    answer = 0
    cnt = 0
    graph = [[] for _ in range(n)]
    visited = [False] * n
    que = PriorityQueue()
    
    for u, v, w in costs:
        graph[u].append([v, w])
        graph[v].append([u, w])
    
    que.put((0, 0))
    while not que.empty() and cnt < n:
        d, node = que.get()
        if visited[node] : continue
        
        visited[node] = True
        answer += d
        cnt += 1
        
        for next, nextD in graph[node]:
            if visited[next] : continue
            que.put((nextD, next))
    
    return answer