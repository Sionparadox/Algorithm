import sys
from collections import deque
input = sys.stdin.readline

def BFS(node):
    queue = deque([node])
    visited[node] = 1
    while queue:
        curr = queue.popleft()
        k = visited[curr]
        
        for nxt in graph[curr]:
            if visited[nxt] == 0:
                visited[nxt] = 3-k
                queue.append(nxt)
            elif visited[nxt] == k:
                return False
    
    return True

T = int(input())
for _ in range(T):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V)]
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    
    visited = [0]*V
    answer = True
    for node in range(V):
        if not visited[node]:
            if not BFS(node):
                answer = False
                break
    
    print("YES" if answer else "NO")

'''
노드 하나씩 마킹(1,2)
다음 노드가 같은 마킹이 있으면 False
'''        