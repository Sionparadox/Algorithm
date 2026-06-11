INF = float('inf')
TC = int(input())
for tc in range(1, TC+1):
    N, A, B = map(int, input().split())
    answer = INF
    for R in range(1, int(N**(0.5))+1):
        for C in range(R, N//R +1):
            answer = min(answer, A*(C-R) + B*(N-R*C))
    
    print(f'#{tc} {answer}')