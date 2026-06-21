def backtrack(node, k):
    res = k
    for nxt in graph[node]:
        if visited[nxt]:
            continue
        visited[nxt] = True
        res = max(res, backtrack(nxt, k+1))
        visited[nxt] = False
        
    return res
    
TC = int(input())
for tc in range(1, TC+1):
    N, K = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(K):
        arr = list(map(int, input().split()))
        for i in range(1, arr[0]):
            graph[arr[i]].append(arr[i+1])
    
    answer = [len(set(x)) for x in graph[1:]]
    graph[0] = list(range(1, N+1))
    visited = [False]*(N+1)
    dist = backtrack(0, 0)
    print(f'#{tc}', *answer, dist)