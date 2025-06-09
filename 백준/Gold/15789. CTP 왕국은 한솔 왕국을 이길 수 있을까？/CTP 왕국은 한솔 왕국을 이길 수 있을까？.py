import sys
from collections import Counter
input = sys.stdin.readline

N, M = map(int, input().split())
parent = [x for x in range(N+1)]

def find(node):
    if parent[node] == node:
        return node
    parent[node] = find(parent[node])
    return parent[node]

def union(u, v):
    rootU = find(u)
    rootV = find(v)
    if rootU != rootV:
        parent[rootU] = rootV

for _ in range(M):
    u, v = map(int, input().split())
    union(u, v)

C, H, K = map(int, input().split())

for i in range(1, N+1):
    find(i)

counter = Counter(parent[1:])
arr = sorted(counter.items(), key=lambda x:-x[1])

cnt = 0
C = find(C)
H = find(H)
answer = counter[C]

for key, value in arr:
    if cnt >= K:
        break
    if key == C or key == H:
        continue
    cnt += 1
    answer += value

print(answer)