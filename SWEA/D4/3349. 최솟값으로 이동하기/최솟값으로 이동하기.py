TC = int(input())
for tc in range(1, TC+1):
    W, H, N = map(int, input().split())
    route = [tuple(map(int, input().split())) for _ in range(N)]
    answer = 0
    for i in range(N-1):
        x, y = route[i]
        nx, ny = route[i+1]
        if (nx-x)*(ny-y)>0:
            answer += max(abs(nx-x), abs(ny-y))
        else:
            answer += abs(nx-x)+abs(ny-y)
    
    print(f'#{tc} {answer}')