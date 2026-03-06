import sys
input = sys.stdin.readline

def find(node):
    if parent[node] == node:
        return node
    parent[node] = find(parent[node])
    return parent[node]

def union(u, v):
    u, v = find(u), find(v)
    if u != v:
        parent[v] = u

T = int(input())
for t in range(1, T+1):
    N = int(input())
    parent = [x for x in range(N)]
    
    K = int(input())
    for _ in range(K):
        u, v = map(int, input().split())
        union(u, v)
    
    print(f'Scenario {t}:')
    M = int(input())
    for _ in range(M):
        u, v = map(int, input().split())
        if find(u) == find(v):
            print(1)
        else:
            print(0)
    print()
            