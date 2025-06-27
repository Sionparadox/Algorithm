import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input())

graph = defaultdict(list)
for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False]*(N+1)

answer = 0
def DFS(node):
    global answer
    res = 1
    for nxt in graph[node]:
        if visited[nxt]:
            continue
        visited[nxt] = True
        size = DFS(nxt)
        answer += size*(size-1)//2 + size*(N-size)
        res += size
    return res

visited[1] = True
DFS(1)
print(answer)
'''
node i 에 대해 i의 부모 pi->i에 대해서
i를 루트로하는 서브트리 내의 움직임은 해당 간선을 지남.
서브트리 내의 정점과 외부 정점간 움직임도 간선을 지남
서브트리 내의 정점의 수 k에 대해
kC2 + k*(N-k)
'''