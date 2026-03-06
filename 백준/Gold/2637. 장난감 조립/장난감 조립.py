import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
M = int(input())
indegree =[0]*(N+1)
need = [0]*(N+1)
graph = [[] for _ in range(N+1)]
advanced = set()

for _ in range(M):
    part, ingredient, k = map(int, input().split())
    indegree[ingredient] += 1
    graph[part].append((ingredient, k))
    advanced.add(part)

need[N] = 1
queue = deque([N])

while queue:
    curr = queue.popleft()
    for nxt, k in graph[curr]:
        indegree[nxt] -= 1
        need[nxt] += need[curr]*k
        if indegree[nxt] == 0:
            queue.append(nxt)

for i in range(1, N+1):
    if i not in advanced:
        print(i, need[i])