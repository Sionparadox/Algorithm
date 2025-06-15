import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

answer = 1
inc_dp = [1]*N
dec_dp = [1]*N

for i in range(1, N):
    if nums[i] >= nums[i-1]:
        inc_dp[i] = inc_dp[i-1]+1
    if nums[i] <= nums[i-1]:
        dec_dp[i] = dec_dp[i-1]+1

print(max(max(inc_dp), max(dec_dp)))