import sys
input = sys.stdin.readline

N, M, Q = map(int, input().split())
connect = [tuple(map(int, input().split())) for _ in range(M)]
deleted = [int(input())-1 for _ in range(Q)]

parent = [x for x in range(N+1)]
size = [1]*(N+1)

def find(node):
    if node == parent[node]:
        return node
    parent[node] = find(parent[node])
    return parent[node]

def union(u, v):
    u, v = find(u), find(v)
    if u == v:
        return 0
    
    res = size[u] * size[v]
    if size[u] < size[v]:
        parent[u] = v
        size[v] += size[u]
    else:
        parent[v] = u
        size[u] += size[v]

    return res

ds = set(deleted)
for i in range(M):
    if i not in ds:
        u, v = connect[i]
        union(u, v)
    
answer = 0
for d in deleted[::-1]:
    u, v = connect[d]
    answer += union(u, v)
print(answer)


'''
100,000번씩이라 N^2 불가능
연결을 나열한 후
제거되지 않을 연결들을 연결함.
이후 제거될 연결을 역순으로 하나씩 연결하며 비용 계산.
'''