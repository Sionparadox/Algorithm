import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

def updateStrahler(node):
    maxVal = 0
    cnt = 0
    for prev in reversed_graph[node]:
        if strahler[prev] > maxVal:
            maxVal = strahler[prev]
            cnt = 1
        elif strahler[prev] == maxVal:
            cnt += 1
    if cnt > 1:
        strahler[node] = maxVal+1
    else:
        strahler[node] = maxVal

for _ in range(T):
    K, M, P = map(int, input().split())
    indegree = [0]*M
    graph = [[] for _ in range(M)]
    reversed_graph = [[] for _ in range(M)]
    strahler = [0]*M
    for _ in range(P):
        A, B = map(int, input().split())
        graph[A-1].append(B-1)
        reversed_graph[B-1].append(A-1)
        indegree[B-1] += 1
    
    queue = deque()
    for i in range(M):
        if indegree[i] == 0:
            queue.append(i)
            strahler[i] = 1
    
    while queue:
        now = queue.popleft()
        
        for next in graph[now]:
            indegree[next] -= 1
            if indegree[next] == 0:
                queue.append(next)
                updateStrahler(next)
    
    print(K, max(strahler))
