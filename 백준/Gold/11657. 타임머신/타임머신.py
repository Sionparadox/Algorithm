import sys
input = sys.stdin.readline
INF = float('inf')

N, M = map(int, input().split())
graph = []
for _ in range(M):
    s, e, t = map(int, input().split())
    graph.append((s, e, t))

def bellman_ford(start):
    dist = [INF]*(N+1)
    dist[start] = 0
    for i in range(N):
        for j in range(M):
            s, e, t = graph[j]
            if dist[s] != INF and dist[e] > dist[s]+t:
                dist[e] = dist[s]+t
                if i == N-1:
                    return [-1]
    return dist[2:]

ans = bellman_ford(1)
for k in ans:
    if k == INF:
        print(-1)
    else:    
        print(k)