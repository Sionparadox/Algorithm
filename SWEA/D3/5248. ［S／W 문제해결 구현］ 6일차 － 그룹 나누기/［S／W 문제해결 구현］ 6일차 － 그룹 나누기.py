T = int(input())
def find(node):
    if node != parent[node]:
        parent[node] = find(parent[node])
    return parent[node]

def union(u, v):
    u, v = find(u), find(v)
    if u != v:
        parent[v] = u

for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    parent = list(range(N+1))
    for i in range(0, M*2, 2):
        union(arr[i], arr[i+1])
    
    groups = set()
    for i in range(1, N+1):
        groups.add(find(i))
    print(f'#{t} {len(groups)}')
    