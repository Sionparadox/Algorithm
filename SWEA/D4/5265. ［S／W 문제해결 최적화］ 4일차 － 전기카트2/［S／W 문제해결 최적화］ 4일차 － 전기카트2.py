INF = float('inf')
def dfs(node, mask):
    if mask == (1<<N)-1:
        return board[node][0]
    
    if dp[node][mask] != INF:
        return dp[node][mask]
    
    for nxt in range(1, N):
        if not (mask & (1<<nxt)):
            dp[node][mask] = min(dp[node][mask], dfs(nxt, mask | (1<<nxt)) + board[node][nxt])
    
    return dp[node][mask]
    

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    dp = [[INF]*(1<<N) for _ in range(N)]
    print(f'#{tc} {dfs(0, 1)}')