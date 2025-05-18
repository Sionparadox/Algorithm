import sys
input = sys.stdin.readline

def bellman_ford(start, graph):
    dist = [0]*(N+1)
    
    for i in range(N):
        for u, v, w in graph:
            if dist[v] > dist[u]+w:
                dist[v] = dist[u]+w
                if i == N-1:
                    return True
    return False
        
    

TC = int(input())
for _ in range(TC):
    N, M, W = map(int, input().split())
    graph = []
    for _ in range(M):
        S, E, T = map(int, input().split())
        graph.append((S,E,T))
        graph.append((E,S,T))
    for _ in range(W):
        S, E, T = map(int, input().split())
        graph.append((S,E,-T))
    
    for i in range(1,N+1):
        graph.append((0, i, 0))
    print("YES" if bellman_ford(0, graph) else "NO")
            
    
