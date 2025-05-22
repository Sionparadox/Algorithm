import sys
input = sys.stdin.readline

A, B = map(int, input().split())
dp = [0, 1]
for i in range(2, 70):
    dp.append(dp[i-1]*2 + 2**(i-1))

def countOne(n):
    if n == 0:
        return 0
    _n = n
    k = 0
    while _n>0:
        _n //= 2
        k += 1
    k -= 1
    return dp[k] + n-2**k+1 + countOne(n-2**k)

print(countOne(B)-countOne(A-1))