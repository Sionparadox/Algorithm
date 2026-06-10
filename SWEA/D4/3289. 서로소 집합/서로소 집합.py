def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def union(u, v):
    u, v = find(u), find(v)
    if u != v:
        parent[v] = u

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    parent = list(range(N+1))
    res = ''
    for _ in range(M):
        cmd, x, y = map(int, input().split())
        if cmd:
           res += '1' if find(x) == find(y) else '0'
        else:
            union(x, y) 
    print(f'#{tc} {res}')
