import sys
import bisect
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

dp = []
pos = []
parent = [-1]*N
for i in range(N):
    idx = bisect.bisect_left(dp, arr[i])
    
    if idx==len(dp):
        dp.append(arr[i])
        pos.append(i)
    else:
        dp[idx] = arr[i]
        pos[idx] = i
    if idx > 0:
        parent[i] = pos[idx-1]

L = len(dp)
answer = []
curr = pos[-1]
while curr != -1:
    answer.append(arr[curr])
    curr = parent[curr]
answer.reverse()
print(L)
print(*answer)