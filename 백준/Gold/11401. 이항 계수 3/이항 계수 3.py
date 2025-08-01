import sys
input = sys.stdin.readline
MOD = 1_000_000_007

N, K = map(int, input().split())
factorial = [1]*(N+1)
for i in range(1, N+1):
    factorial[i] = (factorial[i-1]*i)%MOD

def solve(n, exp):
    if exp == 1:
        return n
    
    half = solve(n, exp//2)
    half = (half**2) % MOD
    if exp % 2 == 1:
        half = (half*n) % MOD
    return half
    

def modinv(n):
    return solve(n, MOD-2)

answer = factorial[N] * modinv(factorial[K]) % MOD
answer = answer * modinv(factorial[N - K]) % MOD
print(answer)


'''
nCk = n!/k!(n-k)!
nCk % MOD = n! * k!^-1 * (n-k)!^-1 %MOD
'''