import sys
input = sys.stdin.readline
N, M = map(int, input().split())
nums = [int(input()) for _ in range(N)]
nums.sort()

answer = nums[-1]-nums[0]
j = 0
for i in range(N):
    while j<N and nums[i] - nums[j] >= M:
        answer = min(answer, nums[i]-nums[j])
        j += 1
print(answer)
    
