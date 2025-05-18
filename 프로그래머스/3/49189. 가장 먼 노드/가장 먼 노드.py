from collections import deque, defaultdict
INF = float('inf')
def solution(n, edge):
    graph = defaultdict(list)
    for u, v in edge:
        graph[u].append(v)
        graph[v].append(u)
        
    dist = [INF] * (n+1)
    queue = deque()
    queue.append(1)
    dist[1] = 0
    dist[0] = 0
    maxVal = 0
    while queue:
        node = queue.popleft()
        maxVal = dist[node]
        for next in graph[node]:
            if dist[next] == INF:
                queue.append(next)
                dist[next] = dist[node]+1
    return dist.count(maxVal)