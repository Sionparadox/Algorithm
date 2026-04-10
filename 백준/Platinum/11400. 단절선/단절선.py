import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0]*(V+1)
cnt = 0
answer = set()

def dfs(node, parent):
    global cnt
    cnt += 1
    visited[node] = cnt
    low = cnt
    
    for nxt in graph[node]:
        if nxt == parent:
            continue
        
        if visited[nxt] == 0:
            child_low = dfs(nxt, node)
            
            if visited[node] < child_low:
                if node < nxt:
                    answer.add((node, nxt))
                else:
                    answer.add((nxt, node))
                    
            
            low = min(low, child_low)
            
        else:
            low = min(low, visited[nxt])
    
    return low

for x in range(1, V+1):
    if visited[x] == 0:
        dfs(x, 0)

print(len(answer))
for u, v in sorted(answer):
    print(u, v)

'''
현재 위치로 올 수 있으면 단절선이 아니므로 단절점 로직에서 등호는 빠져야함.
'''