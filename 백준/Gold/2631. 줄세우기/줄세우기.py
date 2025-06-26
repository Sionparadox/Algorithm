import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]

dp = []
for num in arr:
    idx = bisect_left(dp, num)
    if idx == len(dp):
        dp.append(num)
    else:
        dp[idx] = num
print(N-len(dp))

'''
오름차순으로 배치된 아이들의 수의 최대를 구한 후 (LIS)
전체 길이에서 빼기
'''