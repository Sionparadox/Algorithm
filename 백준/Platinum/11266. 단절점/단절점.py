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

def dfs(node, parent, is_root=False):
    global cnt
    cnt += 1
    visited[node] = cnt
    low = cnt
    child_cnt = 0
    
    for nxt in graph[node]:
        if nxt == parent:
            continue
        
        if visited[nxt] == 0:
            child_cnt += 1
            child_low = dfs(nxt, node)
            
            if not is_root and visited[node] <= child_low:
                answer.add(node)
            
            low = min(low, child_low)
            
        else:
            low = min(low, visited[nxt])
    
    if is_root and child_cnt >=2:
        answer.add(node)
    
    return low

for x in range(1, V+1):
    if visited[x] == 0:
        dfs(x, 0, True)

print(len(answer))
print(*sorted(answer))