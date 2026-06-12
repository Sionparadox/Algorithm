MAX = 999
is_prime = [True]*(MAX+1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(MAX**(0.5))+1):
    if is_prime[i]:
        for j in range(i*i, MAX+1, i):
            is_prime[j] = False

primes = []
for n in range(2, MAX+1):
    if is_prime[n]:
        primes.append(n)

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    answer = 0
    for x in primes:
        if x > N//3:
            break
        for y in range(x,(N-x)//2+1):
            z = N-x-y
            if is_prime[y] and is_prime[z]:
                
                answer += 1
    
    print(F'#{tc} {answer}')