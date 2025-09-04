import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, K = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(K):
    r, c = map(int, input().split())
    graph[r].append(c)

now = [-1]*(N+1)
def binary_matching(node):
    for col in graph[node]:
        if visited[col]: continue
        visited[col] = True
        if now[col] == -1 or binary_matching(now[col]):
            now[col] = node
            return True
    return False

answer = 0
for row in range(1,N+1):
    visited = [False]*(N+1)
    if binary_matching(row):
        answer += 1

print(answer)