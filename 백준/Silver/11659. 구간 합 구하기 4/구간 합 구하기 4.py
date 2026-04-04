import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
prefix = [0]
for x in nums:
    prefix.append(prefix[-1]+x)

for _ in range(M):
    i, j = map(int, input().split())
    print(prefix[j]-prefix[i-1])
