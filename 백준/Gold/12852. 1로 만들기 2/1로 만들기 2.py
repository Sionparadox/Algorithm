import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
parent = [-1]*(N+1)

queue = deque([(N, 0)])
while queue:
    x, cnt = queue.popleft()
    if x == 1:
        break
    if x%3 == 0 and parent[x//3] == -1:
        parent[x//3] = x
        queue.append((x//3,cnt+1))
    if x%2 == 0 and parent[x//2] == -1:
        parent[x//2] = x
        queue.append((x//2, cnt+1))
    if parent[x-1] == -1:
        parent[x-1] = x
        queue.append((x-1, cnt+1))

path = [1]
while x != N:
    x = parent[x]
    path.append(x)

print(cnt)
print(*reversed(path))


'''
BFS로 parent 갱신하며 돌리기
'''