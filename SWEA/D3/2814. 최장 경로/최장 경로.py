def dfs(node, mask, k):
    global answer
    answer = max(answer, k)
    
    for nxt in edges[node]:
        if not (mask & (1<<nxt)):
            dfs(nxt, mask | (1<<nxt), k+1)

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    edges = [set() for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        edges[u-1].add(v-1)
        edges[v-1].add(u-1)
    answer = 0
    
    for i in range(N):
        dfs(i, (1<<i), 1)
    
    print(f'#{tc} {answer}')
    