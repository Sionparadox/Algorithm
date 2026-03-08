import sys
input = sys.stdin.readline

T = int(input())

def find(node):
    if node == parent[node]:
        return node
    root = find(parent[node])
    dist[node] += dist[parent[node]]
    parent[node] = root
    return parent[node]

def union(u, v):
    parent[u] = v
    dist[u] = abs(u-v)%1000

for _ in range(T):
    N = int(input())
    parent = [x for x in range(N+1)]
    dist = [0]*(N+1)
    while True:
        cmd = input().split()
        if cmd[0] == 'O':
            break
        if cmd[0] == 'E':
            k = int(cmd[1])
            find(k)
            print(dist[k])
        else:
            u, v = map(int, cmd[1:])
            union(u, v)
    