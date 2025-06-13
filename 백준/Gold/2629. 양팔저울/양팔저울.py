import sys
input = sys.stdin.readline

N = int(input())
weights = list(map(int, input().split()))
M = int(input())
balls = list(map(int, input().split()))

dp = [set() for _ in range(N+1)]
dp[0].add(0)

for i in range(N):
    w = weights[i]
    for val in dp[i]:
        dp[i+1].add(val)
        dp[i+1].add(val+w)
        dp[i+1].add(abs(val-w))

answer = []
for ball in balls:
    if ball in dp[N]:
        answer.append('Y')
    else:
        answer.append('N')
print(' '.join(answer))
'''
dp[i] : i무게의 구슬까지 탐색했을 때 가능한 무게들

'''