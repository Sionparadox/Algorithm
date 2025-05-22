import sys
input = sys.stdin.readline

G = int(input())
P = int(input())
arr = [int(input()) for _ in range(P)]
parent = [i for i in range(G+1)]

def find(node):
    if parent[node] == node:
        return node
    parent[node] = find(parent[node])
    return parent[node]

def union(u, v):
    parent[find(u)] = find(v)

answer = 0
for g in arr:
    gate = find(g)
    if gate == 0:
        break
    
    answer += 1
    union(gate, gate-1)
    
print(answer)