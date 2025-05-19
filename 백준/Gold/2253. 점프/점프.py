import sys
input = sys.stdin.readline
N, M = map(int, input().split())
small = set(int(input()) for _ in range(M))

for l in range(N):
    if (l**2+l)//2+1 > N:
        break
J = l-1
dp = [[float('inf')]*(J+2) for _ in range(N+1)]
dp[1][0] = 0
if 2 not in small:
    dp[2][1] = 1

for i in range(3, N+1):
    if i in small:
        continue
    
    for j in range(1, min(i, J)+1):
        dp[i][j] = min(dp[i][j], dp[i-j][j-1], dp[i-j][j],dp[i-j][j+1])+1
answer = min(dp[N])
print(answer if answer != float('inf') else -1)
