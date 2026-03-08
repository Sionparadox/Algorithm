import sys
input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]
nums.sort()

presum = set()
for i in nums:
    for j in nums:
        presum.add(i+j)

for i in range(N-1, -1, -1):
    for j in range(i+1):
        diff = nums[i] - nums[j]
        if diff in presum:
            print(nums[i])
            exit()

'''
x+y+z = k
x+y 집합을 만듬
N^3 -> N^2 *2
'''