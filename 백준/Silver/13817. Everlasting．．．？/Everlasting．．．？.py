import sys
input = sys.stdin.readline
MAX = 1000001
primes = []
isPrime = [True]*(MAX+1)
isPrime[0] = isPrime[1] = False
for i in range(2, int(MAX ** 0.5)+1):
    if isPrime[i]:
        for j in range(i*i, MAX, i):
            isPrime[j] = False

for i in range(2, MAX):
    if isPrime[i]:
        primes.append(i)

primeSet = set(primes)

def calc(n):
    factors = []
    for p in primes:
        if p**2>n:
            break
        if n%p == 0:
            factors.append(p)
            while n%p == 0:
                n //= p
    
    if n>1:
        factors.append(n)
    
    if len(factors) == 1:
        return factors[0]
    
    res = factors[-1]
    for f in factors[:-1]:
        res -= f
    
    return res

while True:
    a, b = map(int, input().split())
    if a==0 and b==0:
        break
    a = calc(a)
    b = calc(b)
    if a<b:
        print('b')
    else :
        print('a')
    
    