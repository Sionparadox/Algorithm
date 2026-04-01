import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def find(node):
    if node == parent[node]:
        return node
    
    root = find(parent[node])
    weight[node] += weight[parent[node]]
    parent[node] = root
    
    return parent[node]

def union(u, v, w):
    _u, _v = find(u), find(v)
    if _u != _v:
        parent[_v] = _u
        weight[_v] = weight[u] + w - weight[v]
        

    
while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    parent = list(range(N+1))
    weight = [0]*(N+1)
    
    for _ in range(M):
        cmd = input().strip()
        if cmd[0] == '!':
            x, y, w = map(int, cmd[1:].split())
            union(x, y, w)
        else:
            x, y = map(int, cmd[1:].split())
            if find(x) != find(y):
                print("UNKNOWN")
            else:
                print(weight[y]-weight[x])


'''
분리집합으로 풀되 과정에서 무게 차이를 기록해야함
[4 1 1 4]
1 > 2       [0 100 0 0]
2 > 3       [0 100 200 0]
4 > 3       [-50 100 200 0]
find(2)     [-50 50 200 0]
find(3)     [-50 50 150 0]
'''