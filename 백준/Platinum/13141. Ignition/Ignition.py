import sys
input = sys.stdin.readline
INF = float('inf')

N, M = map(int, input().split())
dist = [[INF]*N for _ in range(N)]
graph = [[0]*N for _ in range(N)]
for i in range(N):
    dist[i][i] = 0

for _ in range(M):
    s, e, l = map(int, input().split())
    s, e = s-1, e-1
    dist[s][e] = min(dist[s][e], l)
    dist[e][s] = min(dist[e][s], l)
    graph[s][e] = max(graph[s][e], l)
    graph[e][s] = max(graph[e][s], l)
    

for k in range(N):
    for i in range(N):
        for j in range(N):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

def burn(node):
    res = 0
    for i in range(N):
        ti = dist[node][i]
        for j in range(N):
            if graph[i][j] == 0: continue
            tj = dist[node][j]
            res = max(res, (ti+tj+graph[i][j])/2)
    return res
    
answer = INF
for i in range(N):
    answer = min(answer, burn(i))
            
print('%.1f'%(answer))
