import sys
input = sys.stdin.readline

T, W = map(int, input().split())
plums = [int(input()) for _ in range(T)]

dp = [[0]*(W+1) for _ in range(T+1)]

for t in range(1, T+1):
    for w in range(min(W, t)+1):
        if w == 0:
            dp[t][w] = dp[t-1][w]
        else:
            dp[t][w] = max(dp[t-1][w], dp[t-1][w-1])
        if w%2 != plums[t-1]%2:
            dp[t][w] += 1

print(max(dp[T]))

'''
dp[t][w] : t초동안 w회 움직여서 먹을 수 있는 자두의 최대값
dp[1][0] = 0 dp[1][1] = 1 dp[1][2] = 0
dp[2][0] = 1 dp[2][1] = 1 dp[2][2] = 2
dp[3][0] = 2 dp[3][1] = 1 dp[3][2] = 3
dp[4][0] = 2 dp[4][1] = 3 dp[4][2] = 3

홀수번 바꾸면 2
짝수번 바꾸면 1
'''