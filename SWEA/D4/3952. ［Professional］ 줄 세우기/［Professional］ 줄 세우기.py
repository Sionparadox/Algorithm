from collections import deque
TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    indegree = [0]*(N+1)
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1
    
    queue = deque()
    for i in range(1, N+1):
        if indegree[i] == 0:
            queue.append(i)
            
    answer = []
    while queue:
        curr = queue.popleft()
        answer.append(curr)
        for nxt in graph[curr]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)
    
    print(f'#{tc}', *answer)