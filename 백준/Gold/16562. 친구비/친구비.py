import sys
input = sys.stdin.readline

N, M, k = map(int, input().split())
cost = list(map(int, input().split()))
parent = [x for x in range(N)]

def find(node):
    if node == parent[node]:
        return node
    
    parent[node] = find(parent[node])
    return parent[node]

def union(u, v):
    u, v = find(u), find(v)
    
    if u != v:
        if cost[u] <= cost[v]:
            parent[v] = u
        else:
            parent[u] = v

    
for _ in range(M):
    u, v = map(int, input().split())
    union(u-1, v-1)

answer = 0
for node in range(N):
    if node == parent[node]:
        answer += cost[node]

print(answer if answer <= k else "Oh no")

