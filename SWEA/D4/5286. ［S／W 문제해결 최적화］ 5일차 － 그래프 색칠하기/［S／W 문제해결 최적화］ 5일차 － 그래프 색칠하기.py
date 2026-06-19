
def check(node, c):
    for nxt in edges[node]:
        if color[nxt] == c:
            return False
    return True

def dfs(node):
    if node>N:
        return True
    
    for c in range(M):
        if check(node, c):
            color[node] = c
            if dfs(node+1):
                return True
            color[node] = -1
    
    return False

TC = int(input())
for tc in range(1, TC+1):
    N, E, M = map(int, input().split())
    edges = [[] for _ in range(N+1)]
    for _ in range(E):
        u, v = map(int, input().split())
        edges[u].append(v)
        edges[v].append(u)
    
    color = [-1]*(N+1)
    
    print(f'#{tc} {1 if dfs(1) else 0}')