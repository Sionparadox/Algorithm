import sys
import bisect
input = sys.stdin.readline

N, M, K = map(int, input().split())
cards = list(map(int, input().split()))
reds = list(map(int, input().split()))
cards.sort()

parent = [x for x in range(M+1)]

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

for red in reds:
    idx = bisect.bisect_right(cards, red)
    node = find(idx)
    print(cards[node])
    union(node, node+1)
