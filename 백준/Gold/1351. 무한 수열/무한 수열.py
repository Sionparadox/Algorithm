import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, P, Q = map(int, input().split())
if Q>P : P,Q = Q,P

dp = {0:1}
def solve(n):
    if n in dp: 
        return dp[n]
    l, r = n//P, n//Q
    L = solve(l)
    R = solve(r)
    dp[n] = L+R
    return dp[n]

print(solve(N))

'''
divide and conquer with dp
N//P, N//Q

'''