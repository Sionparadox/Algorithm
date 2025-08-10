import sys
input = sys.stdin.readline

N = int(input())
squares = []
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    if x2<x1:
        x1, x2 = x2, x1
    if y2<y1:
        y1, y2 = y2, y1
    squares.append((x1, y1, x2, y2))

parent = [x for x in range(N)]
is_zero = 0

def find(node):
    if node == parent[node]:
        return node
    parent[node] = find(parent[node])
    return parent[node]

def union(u, v):
    u, v = find(u), find(v)
    if u != v:
        parent[v] = u

def cross_zero(idx):
    x1, y1, x2, y2 = squares[idx]
    if x1 == 0 or x2 == 0:
        if y1*y2 <= 0 :
            return True
    if y1 == 0 or y2 == 0:
        if x1*x2 <= 0:
            return True
    return False

def is_cross(i, j):
    x1, y1, x2, y2 = squares[i]
    x3, y3, x4, y4 = squares[j]
    if x1 < x3 and x4 < x2 and y1 < y3 and y4 < y2:
        return False
    if x3 < x1 and x2 < x4 and y3 < y1 and y2 < y4:
        return False
    return not (x2 < x3 or x4 < x1 or y2 < y3 or y4 < y1)
    
for i in range(N):
    if cross_zero(i):
        is_zero = 1
        break

for i in range(N-1):
    for j in range(i+1, N):
        if is_cross(i, j):
            union(i, j)
           
tmp = set() 
for i in range(N):
    tmp.add(find(i))
answer = len(tmp) + (1-is_zero) -1
print(answer)

'''
겹치지 않는 직사각형 그룹이 몇개
+ 직사각형중 하나가 원점을 지나가는지
원점 지나려면 x,y중 하나가 0이어야하고 다른 하나는 곱이 0이하여야함.
두 사각형이 겹치려면 포함관계 X + 좌표가 하나라도 겹쳐야함.
'''