import sys
input = sys.stdin.readline

N = int(input())
exp = input().strip()

def calc(x,op,y):
    if op == '+':
        return x+y
    if op == '-':
        return x-y
    if op == '*':
        return x*y

max_dp = [[-float('inf')]*N for _ in range(N)]
min_dp = [[float('inf')]*N for _ in range(N)]

for i in range(0, N, 2):
    max_dp[i][i] = int(exp[i])
    min_dp[i][i] = int(exp[i])

for length in range(3, N+1, 2):
    for i in range(0, N-length+1, 2):
        j = i+length-1
        for k in range(i+1, j, 2):
            for x in (max_dp[i][k-1], min_dp[i][k-1]):
                for y in (max_dp[k+1][j], min_dp[k+1][j]):
                    max_dp[i][j] = max(max_dp[i][j], calc(x,exp[k],y))
                    min_dp[i][j] = min(min_dp[i][j], calc(x,exp[k],y))        

print(max_dp[0][N-1])

'''
max_dp[i][j] = i~j사이의 수식을 계산했을 때의 최댓값
min_dp[i][j] = i~j사이의 수식을 계산했을 때의 최솟값
max_dp[i][j] = max(max_dp[i][j],
    calc(max_dp[i][k-1], exp[k], max_dp[k+1][j]),
    calc(max_dp[i][k-1], exp[k], min_dp[k+1][j]),
    calc(min_dp[i][k-1], exp[k], max_dp[k+1][j]),
    calc(min_dp[i][k-1], exp[k], min_dp[k+1][j]))
'''