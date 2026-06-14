TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    graph = [[False]*(N+1) for _ in range(N+1)]
    answer = 0
    for _ in range(M):
        x, y = map(int, input().split())
        for k in range(N+1):
            if graph[x][k] and graph[k][y]:
                answer += 1
        graph[x][y] = graph[y][x] = True
    
    print(f'#{tc} {answer}')