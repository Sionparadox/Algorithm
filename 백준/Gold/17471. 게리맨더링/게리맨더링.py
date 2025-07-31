import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
populations = list(map(int, input().split()))
graph = {}
for i in range(N):
    arr = list(map(int, input().split()))
    graph[i] = []
    for k in arr[1:]:
        graph[i].append(k-1)

def isConnect(group):
    if not group:
        return False
    el = next(iter(group))
    queue = deque([el])
    visited = set([el])
    while queue:
        n = queue.popleft()
        for nxt in graph[n]:
            if nxt in group and nxt not in visited:
                visited.add(nxt)
                queue.append(nxt)
    
    return visited == group

answer = float('inf')
for mask in range(1<<(N-1), 1<<N):
    group1 = {i for i in range(N) if mask & (1 << i)}
    group2 = set(range(N)) - group1
    
    if isConnect(group1) and isConnect(group2):
        s1 = sum(populations[i] for i in group1)
        s2 = sum(populations[i] for i in group2)
        answer = min(answer, abs(s1-s2))

print(answer if answer != float('inf') else -1)

'''
비트마스킹으로 2그룹으로 나눔.
중복 방지를 위해 최상위 비트가 1인 것을 그룹 1로 취급.
'''