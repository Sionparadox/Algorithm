MAX = 1_000_000
is_prime = [True]*(MAX+1)
is_prime[0] = is_prime[1] = False
f = [1]*(MAX+1)

for i in range(3, MAX+1):
    if is_prime[i]:
        for j in range(i, MAX+1, i):
            is_prime[j] = False
            
            k = j
            tmp = 1
            n = i
            while k % i == 0:
                tmp += n
                k //= i
                n *= i
                
            f[j] *= tmp


for i in range(2, MAX+1, 2):
    f[i] = f[i//2]

prefix_sum = [0]*(MAX+1)
for i in range(1, MAX+1):
    prefix_sum[i] = prefix_sum[i-1]+f[i]

TC = int(input())
for tc in range(1, TC+1):
    L, R = map(int, input().split())
    print(f'#{tc} {prefix_sum[R] - prefix_sum[L-1]}')