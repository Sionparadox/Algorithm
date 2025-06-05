import sys
from math import gcd, factorial
input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]
K = int(input())

mods = [x % K for x in nums]
digits = [len(str(x)) for x in nums]
pow10 = [1]*51
for i in range(1, 51):
    pow10[i] = pow10[i-1]*10 % K

dp = [[0]*K for _ in range(1<<N)]

for i in range(N):
    dp[1<<i][mods[i]] = 1

for mask in range(1<<N):
    for mod in range(K):
        if dp[mask][mod] == 0:
            continue
        for i in range(N):
            if not (mask & (1<<i)):
                next = mask | (1<<i)
                newMod = (mod*pow10[digits[i]] + mods[i])%K
                dp[next][newMod] += dp[mask][mod]

answer = dp[(1<<N) -1][0]
f = factorial(N)
gcd = gcd(answer ,f)
p = answer//gcd
q = f//gcd
print(f'{p}/{q}')


'''
100 % 7 = 2
10 % 7 = 3
2*100 + 3 = 203 % 7 = 0
10010 % 7 = 0

비트마스킹으로 dp?
dp[mask][mod] : mask로 선택된 수를 이어 만드는 수열중 나머지가 mod인 경우의 수


'''