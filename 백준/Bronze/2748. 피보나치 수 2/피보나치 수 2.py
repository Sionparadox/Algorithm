import sys
input = sys.stdin.readline

dp = [0, 1]
N = int(input())
for i in range(2, N+1):
    dp.append(dp[-1]+dp[-2])
print(dp[-1])