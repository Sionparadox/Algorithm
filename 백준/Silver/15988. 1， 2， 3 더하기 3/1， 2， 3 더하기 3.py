import sys
input = sys.stdin.readline
MOD = 1000000009

T = int(input())
nums = [int(input()) for _ in range(T)]
max_num = max(nums)
dp = [0]*(max(max_num,3)+1)
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, max_num+1):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3])%MOD

for n in nums:
    print(dp[n])

'''
1 : 1
2 : 1+1, 2 -> 2
3 : 1+1+1, 1+2, 2+1, 3 -> 4
4 : 1111, 112, 121, 211, 13, 22, 31 -> 7
5 : 11111, 1112, 1121, 1211, 2111, 113, 131, 311, 122, 212, 221, 23, 32 -> 13
dp[n] = dp[n-1] + dp[n-2] + dp[n-3]
'''