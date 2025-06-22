import sys
input = sys.stdin.readline
         
T = int(input())
TC = [int(input()) for _ in range(T)]
maxT = max(TC)
dp = [0]*(maxT+1)
dp[0] = 1
for i in range(1,4):
    for j in range(i, maxT+1):
        dp[j] += dp[j-i]
    
for tc in TC:
    print(dp[tc])
'''
dp[i] : i를 만드는 경우의 수
'''