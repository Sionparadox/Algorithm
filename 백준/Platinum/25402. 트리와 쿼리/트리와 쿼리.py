import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

tree = list(range(N+1))
tree[1] = 0
queue = deque([1])
while queue:
    curr = queue.popleft()
    for nxt in graph[curr]:
        if tree[nxt] != nxt:
            continue
        tree[nxt] = curr
        queue.append(nxt)

target = [False]*(N+1)
parent = list(range(N+1))
size = [1]*(N+1)

def find(node):
    if parent[node] == node:
        return node
    parent[node] = find(parent[node])
    return parent[node]

def union(u, v):
    u, v = find(u), find(v)
    if u == v:
        pass
    if size[u] > size[v]:
        u, v = v, u
    parent[v] = u
    size[u] += size[v]
    
def rollback(arr):
    for node in arr:
        target[node] = False
        parent[node] = node
        size[node] = 1

Q = int(input())
for i in range(Q):
    _input = list(map(int, input().split()))
    K = _input[0]
    S = _input[1:]
    for node in S:
        target[node] = True
    
    for node in S:
        p = tree[node]
        if target[p]:
            union(node, p)
    
    answer = 0
    for node in S:
        if parent[node] == node:
            answer += size[node] * (size[node]-1) // 2

    print(answer)
    rollback(S)
    
    

'''
트리 : 사이클x
1을 루트로 하는 트리 생성
parent, size 배열 재생성 << 시간초과
-> 재활용
'''