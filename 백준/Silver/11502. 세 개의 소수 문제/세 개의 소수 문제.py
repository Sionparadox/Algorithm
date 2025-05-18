import sys
input = sys.stdin.readline
isPrime = [True]*1001
isPrime[0] = isPrime[1] = False
for i in range(2,int(1000 ** 0.5)+1):
    if isPrime[i]:
        for j in range(i**2, 1001, i):
            isPrime[j] = False
primes = []
primeSet = set()
for i in range(3,1001):
    if isPrime[i]:
        primes.append(i)
        primeSet.add(i)
L = len(primes)

def canPrimeSum(n):
    for i in range(L):
        if primes[i]>=N : break
        for j in range(i, L):
            if n-primes[i]-primes[j] in primeSet:
                print(primes[i], primes[j], n-primes[i]-primes[j])
                return True
    return False

T = int(input())
for _ in range(T):
    N = int(input())
    if N-4 in primeSet:
        print(2,2,N-4)
        continue
    if not canPrimeSum(N):
        print(0)
   