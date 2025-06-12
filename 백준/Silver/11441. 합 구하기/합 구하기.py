import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
prefix = [0]*(N+1)
for i in range(N):
    prefix[i+1] = prefix[i]+nums[i]

M = int(input())

for _ in range(M):
    s, e = map(int, input().split())
    print(prefix[e] - prefix[s-1])