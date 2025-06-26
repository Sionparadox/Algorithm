import sys
input = sys.stdin.readline

N, M = map(int, input().split())
mars = [list(map(int, input().split())) for _ in range(N)]

dp = [0] * M
dp[0] = mars[0][0]
for i in range(1, M):
    dp[i] = dp[i-1] + mars[0][i]

for r in range(1, N):
    left = [-float('inf')] * M
    right = [-float('inf')] * M
    
    left[0] = dp[0]+mars[r][0]
    for c in range(1, M):
        left[c] = max(dp[c], left[c-1])+mars[r][c]
    
    right[M-1] = dp[M-1] + mars[r][M-1]
    for c in range(M-2, -1, -1):
        right[c] = max(dp[c], right[c+1])+mars[r][c]
    
    for c in range(M):
        dp[c] = max(left[c], right[c])

print(dp[M-1])
    
'''
이번에 우측이동 했다면 다음엔 우,하만 가능
이번에 좌측이동 했다면 다음엔 좌,하만 가능
이번에 하단이동 했다면 다음엔 전부 가능
dp + dfs << 시간초과
행에 대해 반복하며 우측이동, 좌측이동 할 수 있는 경우를 따져서 각 행에 대해 dp에 최대값 갱신

'''