import sys
from collections import deque
input = sys.stdin.readline

N, P = map(int, input().split())
capacity = [[0]*N for _ in range(N)]
for _ in range(P):
    s, e = map(int, input().split())
    capacity[s-1][e-1] += 1

flow = [[0]*N for _ in range(N)]
parent = [-1]*N
max_flow = 0
source, sink = 0, 1

def BFS(source, sink):
    visited = [False]*N
    queue = deque([source])
    visited[source] = True
    while queue:
        curr = queue.popleft()
        
        for nxt in range(N):
            if visited[nxt]: continue
            if capacity[curr][nxt] > flow[curr][nxt]:
                visited[nxt] = True
                queue.append(nxt)
                parent[nxt] = curr
                if nxt == sink:
                    return True
    return False

while True:
    if not BFS(source, sink): break
    
    v = sink
    while v != source:
        flow[parent[v]][v] += 1
        flow[v][parent[v]] -= 1
        
        v = parent[v]
    max_flow += 1

print(max_flow)