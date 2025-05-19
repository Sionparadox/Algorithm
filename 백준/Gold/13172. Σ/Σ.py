import sys
input = sys.stdin.readline
MOD = 1000000007

def GCD(x,y):
    if y == 0:
        return x, 1, 0
    
    gcd, a1, b1 = GCD(y, x%y)
    
    a = b1
    b = a1 - (x//y)*b1
    return gcd, a, b

def inverse(n):
    gcd, x, _ = GCD(n, MOD)
    return x%MOD

M = int(input())

answer = 0
for i in range(M):
    N, S = map(int, input().split())
    inv = inverse(N)
    res = (S*inv)%MOD
    answer = (answer+res)%MOD
print(answer)