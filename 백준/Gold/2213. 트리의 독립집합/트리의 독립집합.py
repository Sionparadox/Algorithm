import sys
input = sys.stdin.readline

N = int(input())
weights = list(map(int, input().split()))
graph = [[] for _ in range(N)]
for _ in range(N-1):
    u, v = map(int, input().split())
    u, v = u-1, v-1
    graph[u].append(v)
    graph[v].append(u)


visited = [False]*N
dp = [[0]*2 for _ in range(N)]

def DFS(node):
    visited[node] = True
    dp[node][1] = weights[node]
    for nxt in graph[node]:
        if visited[nxt] : continue
        DFS(nxt)
        dp[node][0] += max(dp[nxt])
        dp[node][1] += dp[nxt][0]

DFS(0)
path = []
visited = [False]*N
def find_path(node, selected):
    visited[node] = True
    if selected:
        path.append(node+1)
        for nxt in graph[node]:
            if visited[nxt] : continue
            find_path(nxt, False)
    else:
        for nxt in graph[node]:
            if visited[nxt] : continue
            if dp[nxt][1]> dp[nxt][0]:
                find_path(nxt, True)
            else:
                find_path(nxt, False)
    

if dp[0][0] > dp[0][1]:
    find_path(0, False)
else:
    find_path(0, True)

print(max(dp[0]))
print(*sorted(path))
