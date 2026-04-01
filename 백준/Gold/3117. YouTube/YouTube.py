import sys
input = sys.stdin.readline

N, K, M = map(int, input().split())
M -= 1
start = list(map(int, input().split()))
LOG = M.bit_length()

parent = [[0]+list(map(int, input().split()))]+[[0]*(K+1) for _ in range(LOG-1)]

for k in range(1, LOG):
    for i in range(1, K+1):
        parent[k][i] = parent[k-1][parent[k-1][i]]


def solve(n):
    for k in range(LOG-1, -1, -1):
        if M & (1<<k):
            n = parent[k][n]
    
    return n

answer = []
memo = {}
for n in start:
    if n not in memo:
        memo[n] = solve(n)

    answer.append(memo[n])

print(*answer)


'''
희소배열 사용해서 log단위로 점프
M분 후 결과라서 M-1값이 답
'''