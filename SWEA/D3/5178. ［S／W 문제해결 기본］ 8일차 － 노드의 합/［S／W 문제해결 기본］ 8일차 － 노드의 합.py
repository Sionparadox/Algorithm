def fill(node):
    if node > N:
        return 0
    if node in tree:
        return tree[node]
    res = 0
    res += fill(node*2)
    res += fill(node*2+1)
    
    tree[node] = res
    return res

T = int(input())
for t in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = {}
    for _ in range(M):
        node, value = map(int, input().split())
        tree[node] = value
    
    print(f'#{t} {fill(L)}')
