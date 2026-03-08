import sys
input = sys.stdin.readline

p, w = map(int, input().split())
start, end = map(int, input().split())
parent = [x for x in range(p)]
graph = []
for _ in range(w):
    graph.append(tuple(map(int, input().split())))

graph.sort(key = lambda x:-x[2])

def find(node):
    if node == parent[node]:
        return node
    parent[node] = find(parent[node])
    return parent[node]

def union(u, v):
    u, v = find(u), find(v)
    if u != v:
        parent[v] = u

for u, v, width in graph:
    union(u, v)
    if find(start) == find(end):
        print(width)
        break
