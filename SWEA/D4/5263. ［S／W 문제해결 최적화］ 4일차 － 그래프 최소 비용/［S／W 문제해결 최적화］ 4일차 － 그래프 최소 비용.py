INF = float('inf')
T = int(input())
for t in range(1, T+1):
    N = int(input())
    dist = [list(map(int, input().split())) for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if i != j and dist[i][j] == 0:
                dist[i][j] = INF
    
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

    print(f'#{t} {max(max(row) for row in dist)}')
    
    