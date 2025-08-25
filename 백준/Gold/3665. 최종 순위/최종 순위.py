import sys
from collections import deque
input = sys.stdin.readline

def solve():
    queue = deque()
    for i in range(1, N+1):
        if indegree[i] == 0:
            queue.append(i)
    res = []
    flag = False
    for i in range(N):
        if not queue:
            print("IMPOSSIBLE")
            return
        if len(queue)>1:
            flag = True
        now = queue.popleft()
        res.append(now)
        for nxt in graph[now]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)
    
    
    if flag: print('?')
    else : print(*res)


T = int(input())
for _ in range(T):
    N = int(input())
    base = list(map(int, input().split()))
    rank = [-1]*(N+1)
    for i in range(N):
        rank[base[i]] = i
    indegree = [0]*(N+1)
    graph = [[] for _ in range(N+1)]
    for i in range(N):
        for j in range(i+1, N):
            graph[base[i]].append(base[j])
            indegree[base[j]] += 1
    
    M = int(input())
    for _ in range(M):
        a, b = map(int, input().split())
        if rank[a] > rank[b]:
            a, b = b, a
        graph[a].remove(b)
        indegree[a] += 1
        graph[b].append(a)
        indegree[b] -= 1
    
    solve()
        
'''
원래 순위로 그래프, 진입차수를 초기화.
이후 입력에 따라 그래프와 진입차수를 변경
'''    