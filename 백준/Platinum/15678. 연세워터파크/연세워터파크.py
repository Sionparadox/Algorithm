import sys
from collections import deque
input = sys.stdin.readline

N, D = map(int, input().split())
nums = list(map(int, input().split()))

dp = [0]*N
dq = deque()
for i in range(N):
    while dq and dq[0] < i-D:
        dq.popleft()
    
    val = nums[i]
    if dq and dp[dq[0]]>0:
        val += dp[dq[0]]
    dp[i] = val
    
    while dq and dp[dq[-1]] < dp[i]:
        dq.pop()
    dq.append(i)

print(max(dp))

'''
dp[i] = max(0, dp[i-k](1<=k<=D))+dp[i]
i에 대해 N번 k에 대해 N번 -> N^2 (X)
deque에 최대값을 가지는 인덱스를 저장
'''