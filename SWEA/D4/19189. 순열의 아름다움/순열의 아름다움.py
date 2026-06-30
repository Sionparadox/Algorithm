TC = int(input())
for tc in range(1, TC+1):
    N, P = map(int, input().split())
    factorial = [1]*(N+1)
    
    for i in range(1, N+1):
        factorial[i] = (factorial[i-1]*i) % P
    answer = 0
    for length in range(1, N+1):
        answer = (answer + pow(N-length+1,2)*factorial[length]*factorial[N-length])%P
    
    print(f'#{tc} {answer}')