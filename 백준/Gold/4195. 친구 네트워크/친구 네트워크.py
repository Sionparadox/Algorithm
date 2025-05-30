import sys
input = sys.stdin.readline


def find(node):
    if parent[node] == node:
        return node
    parent[node] = find(parent[node])
    return parent[node]
    
def union(u, v):
    rootU = find(u)
    rootV = find(v)
    if rootU != rootV:
        parent[rootV] = rootU
        size[rootU] += size[rootV]

T = int(input())
for _ in range(T):
    F = int(input())
    name = {}
    parent = []
    size = []
    idx = 0
    for f in range(F):
        A, B = input().split()
        if A not in name:
            name[A] = idx
            parent.append(idx)
            size.append(1)
            idx += 1
        if B not in name:
            name[B] = idx
            parent.append(idx)
            size.append(1)
            idx += 1
        
        union(name[A], name[B])
        print(size[find(name[A])])
