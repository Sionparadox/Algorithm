MAX = 1_000_000
is_prime = [True]*(MAX+1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(MAX**(0.5))+1):
    if is_prime[i]:
        for j in range(i*i, MAX+1, i):
            is_prime[j] = False



TC = int(input())
for tc in range(1, TC+1):
    D, A, B = map(int, input().split())
    answer = 0
    for i in range(A, B+1):
        if is_prime[i] and str(D) in str(i):
            answer += 1
    
    print(f'#{tc} {answer}')