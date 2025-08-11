import sys
from collections import deque
input = sys.stdin.readline

A, B, C = map(int, input().split())
tot = A+B+C
if tot % 3 != 0:
    print(0)
    exit()

visited = [[False]*(1501) for _ in range(1501)]

A, B, C = sorted([A, B, C])
queue = deque([(A, C)])
visited[A][C] = True

while queue:
    a, c = queue.popleft()
    b = tot-a-c
    if a == b == c:
        print(1)
        exit()
    for x, y in [(a, b), (b, c), (a, c)]:
        if x==y:
            continue
        z = tot-x-y
        y -= x
        x += x
        minV, maxV = min(x,y,z), max(x,y,z)
        if not visited[minV][maxV]:
            visited[minV][maxV] = True
            queue.append((minV, maxV))
print(0)