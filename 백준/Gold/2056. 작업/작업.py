import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
dp = [0]*(N+1)
for i in range(1, N+1):
    _input = list(map(int, input().split()))
    dp[i] = _input[0]
    if _input[1] != 0:
        dp[i] += max(dp[p] for p in _input[2:])
    
print(max(dp))
    
'''
위상정렬을 하려했는데
입력이 이미 정렬된 상태
'''