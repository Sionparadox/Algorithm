import sys
input = sys.stdin.readline

N, K, Q = map(int, input().split())

def parent(node):
    if node == 1:
        return -1
    idx = 1
    k = 1
    while k + idx <= node:
        k += idx
        idx *= K
    
    res = (node-k)//K
    res += k - idx//K
    return res

answer = []
for _ in range(Q):
    u, v = map(int, input().split())
    if K == 1:
        print(abs(u-v))
        continue
    dist = 0
    while True:
        if u == v:
            break
        if u > v:
            u = parent(u)
        else:
            v = parent(v)
        dist += 1
    
    print(dist)