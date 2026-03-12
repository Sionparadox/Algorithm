import sys
input = sys.stdin.readline

def mod_pow(a, d, n):
    res = 1
    while d:
        if d & 1:
            res = res * a % n

        a = (a**2) % n
        d >>= 1
    return res

def miller_rabin(n, a):
    d = n - 1
    s = 0
    
    while d % 2 == 0:
        d //= 2
        s += 1
    
    x = mod_pow(a, d, n)
    
    if x == 1 or x == n-1:
        return True
    
    for _ in range(s-1):
        x = x * x % n
        if x == n-1:
            return True
    
    return False

def is_prime(n):
    if n < 2:
        return False
    
    small = [2,3,5,7,11,13,17]
    
    for p in small:
        if n == p:
            return True
        if n % p == 0:
            return False
    
    for a in small:
        if not miller_rabin(n, a):
            return False
    
    return True

T = int(input())
for _ in range(T):
    N = sum(map(int, input().split()))

    if N < 4:
        print("NO")
    elif N % 2 == 0:
        print("YES")
    else:
        print("YES" if is_prime(N-2) else "NO")


'''
밀러 라빈 소수 판별법?
mod_pow : a^d % n 구하기
이를 통해 x = a^d % n을 구함 
- a : 키로 쓰이는 작은 수
- d : (n-1) = d * 2^s를 만족하는 홀수 d
- n : 소수를 판단할 수
x가 1이나 n-1이면 n은 소수
아니라면
s-1번동안 x = x^2 % n을 하며 n-1이 나오는지 판단

이를 작은수(예: 17이하 소수) a 에 대해 miller_rabin(n, a)를 해서 모두 참이면 소수
'''
