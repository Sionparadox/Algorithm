import sys
input = sys.stdin.readline


N = int(input())

L = int(N**0.5)+1
isPrime = [True]*(L+1)
isPrime[0] = isPrime[1] = False

for i in range(2, L):
    if isPrime[i]:
        for j in range(i*i, L, i):
            isPrime[j] = False

answer = 1
for i in range(2,L):
    if not isPrime[i]:
        continue
    
    cnt = 0
    while N%i == 0:
        N //= i
        cnt += 1
    if cnt > 0:
        answer *= (i-1) * i**(cnt-1)

if N != 1:
    answer *= N-1
print(answer)
    