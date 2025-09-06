import sys
input = sys.stdin.readline
MOD = 1_000_000_007

def inverse(n, exp):
    if exp == 1:
        return n
    
    half = inverse(n, exp//2)
    half = (half**2) % MOD
    if exp % 2 == 1:
        half = (half*n) % MOD
    return half
    

def modinv(n):
    return inverse(n, MOD-2)

factorial = [1]*(4_000_001)
for i in range(1, 4_000_001):
    factorial[i] = (factorial[i-1]*i)%MOD

M = int(input())
for _ in range(M):
    N, K = map(int, input().split())
    ans = factorial[N]
    ans = ans * modinv(factorial[K]) % MOD
    ans = ans * modinv(factorial[N - K]) % MOD
    print(ans)

'''
nCk = n!/k!(n-k)!
nCk % MOD = n! * k!^-1 * (n-k)!^-1 %MOD
'''