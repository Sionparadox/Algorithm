import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
lines = [list(map(int, input().split())) for _ in range(N)]
parent = [x for x in range(N)]

def find(node):
    if parent[node] == node:
        return node
    parent[node] = find(parent[node])
    return parent[node]

def ccw(x1, y1, x2, y2, x3, y3):
    return (x2-x1)*(y3-y1) - (y2-y1)*(x3-x1)

def isCross(l1, l2):
    x1, y1, x2, y2 = lines[l1]
    x3, y3, x4, y4 = lines[l2]
    a = ccw(x1, y1, x2, y2, x3, y3)
    b = ccw(x1, y1, x2, y2, x4, y4)
    c = ccw(x3, y3, x4, y4, x1, y1)
    d = ccw(x3, y3, x4, y4, x2, y2)
    
    if a==0 and b==0 and c==0 and d==0:
        if min(x1,x2)<=max(x3,x4) and min(x3,x4)<=max(x1,x2) and \
        min(y1,y2)<=max(y3,y4) and min(y3,y4)<=max(y1, y2):
            return True
        return False
    
    return a*b <=0 and c*d <= 0

for i in range(N-1):
    for j in range(i+1, N):
        rootI = find(i)
        rootJ = find(j)
        if rootI != rootJ and isCross(i, j):
            parent[rootJ] = find(rootI)

for i in range(N):
    parent[i] = find(i)

counter = Counter(parent)
print(len(counter))
print(max(counter.values()))
    