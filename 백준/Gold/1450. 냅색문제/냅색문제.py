import sys
from bisect import bisect_right
input = sys.stdin.readline

N, C = map(int, input().split())
nums = list(map(int, input().split()))

def getHalfSum(arr):
    n = len(arr)
    res = []
    for i in range(1<<n):
        tmp = 0
        for j in range(n):
            if i & (1<<j):
                tmp += arr[j]
        res.append(tmp)
    return res

left = getHalfSum(nums[:N//2])
right = getHalfSum(nums[N//2:])
right.sort()

ans = 0
for val in left:
    ans += bisect_right(right, C-val)
print(ans)
