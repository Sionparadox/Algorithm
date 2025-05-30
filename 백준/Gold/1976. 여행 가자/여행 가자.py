import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
cities = list(map(int, input().split()))
parent = [x for x in range(N)]

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

for i in range(N-1):
    for j in range(i+1, N):
        if graph[i][j] == 1:
            union(i, j)

key = find(cities[0]-1)
answer = "YES"
for i in cities:
    if find(i-1) != key:
        answer = "NO"
        break
print(answer)
 