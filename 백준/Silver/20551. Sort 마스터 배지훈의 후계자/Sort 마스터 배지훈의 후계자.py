import sys
import bisect
input = sys.stdin.readline

N, M = map(int, input().split())
nums = [int(input()) for _ in range(N)]
targets = [int(input()) for _ in range(M)]
nums.sort()

for target in targets:
    idx = bisect.bisect_left(nums, target)
    if idx < N and nums[idx] == target:
        print(idx)
    else :
        print(-1)