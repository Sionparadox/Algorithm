import sys
import bisect
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))

dp = []
for num in A:
    idx = bisect.bisect_left(dp, num)
    
    if idx == len(dp):
        dp.append(num)
    else :
        dp[idx] = num
print(len(dp))