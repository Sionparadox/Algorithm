import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v, d = map(int, input().split())
    graph[u].append((v, d))
    graph[v].append((u, d))


def BFS(node, target):
    visited = [False]*(N+1)
    visited[node] = True
    queue = deque([(node, 0)])
    while queue:
        curr, dist = queue.popleft()
        if curr == target:
            return dist
        for nxt, d in graph[curr]:
            if not visited[nxt]:
                visited[nxt] = True
                queue.append((nxt, dist+d))
    
    return -1

for _ in range(M):
    u, v = map(int, input().split())
    print(BFS(u, v))
