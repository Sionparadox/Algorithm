import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
M = int(input())

def find(node):
    if node == parent[node]:
        return node
    parent[node] = find(parent[node])
    return parent[node]

def union(u, v):
    rootU, rootV = find(u), find(v)
    if rootU != rootV:
        parent[rootV] = rootU
        
enemy = defaultdict(list)
parent = [x for x in range(N+1)]
for _ in range(M):
    type, u, v = input().split()
    u, v = int(u), int(v)
    if type == 'F':
        union(u, v)
    else:
        enemy[u].append(v)
        enemy[v].append(u)

for i in enemy.keys():
    for e in enemy[i]:
        for f in enemy[e]:
            union(i, f)

cnt = set()
for p in parent[1:]:
    p = find(p)
    if p not in cnt:
        cnt.add(p)

print(len(cnt))
